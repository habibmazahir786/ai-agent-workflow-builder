"""Small, dependency-free sequential AI workflow engine."""
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

VARIABLE = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_.]*)\s*\}\}")


class WorkflowError(Exception):
    """Invalid workflow configuration or execution failure."""


def render(value, context):
    if isinstance(value, str):
        def substitute(match):
            path = match.group(1)
            current = context
            for key in path.split('.'):
                if not isinstance(current, dict) or key not in current:
                    raise WorkflowError(f"Unknown variable: {path}")
                current = current[key]
            return str(current)
        return VARIABLE.sub(substitute, value)
    if isinstance(value, list):
        return [render(item, context) for item in value]
    if isinstance(value, dict):
        return {key: render(item, context) for key, item in value.items()}
    return value


def openai_text(prompt, model):
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise WorkflowError('OPENAI_API_KEY is required for openai steps')
    if not isinstance(model, str) or not re.fullmatch(r'[A-Za-z0-9._-]{1,100}', model):
        raise WorkflowError('Invalid model name')
    payload = json.dumps({'model': model, 'input': prompt}).encode('utf-8')
    request = urllib.request.Request(
        'https://api.openai.com/v1/responses', data=payload,
        headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
        method='POST')
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        raise WorkflowError(f'OpenAI request failed (HTTP {exc.code})') from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise WorkflowError('OpenAI request failed (network error or timeout)') from exc
    parts = [content.get('text', '') for item in result.get('output', [])
             if item.get('type') == 'message'
             for content in item.get('content', []) if content.get('type') == 'output_text']
    if not parts:
        raise WorkflowError('OpenAI returned no text output')
    return '\n'.join(parts)


def run_workflow(config, inputs=None):
    if not isinstance(config, dict) or not isinstance(config.get('steps'), list) or not config['steps']:
        raise WorkflowError('Workflow must contain a nonempty steps list')
    context = {'input': inputs or {}, 'steps': {}}
    for number, step in enumerate(config['steps'], start=1):
        if not isinstance(step, dict):
            raise WorkflowError(f'Step {number} must be an object')
        name = step.get('id')
        if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', name):
            raise WorkflowError(f'Step {number} has an invalid id')
        if name in context['steps']:
            raise WorkflowError(f'Duplicate step id: {name}')
        kind = step.get('type')
        try:
            if kind == 'template':
                output = render(step['template'], context)
            elif kind == 'uppercase':
                output = str(render(step['text'], context)).upper()
            elif kind == 'openai':
                prompt = str(render(step['prompt'], context))
                output = openai_text(prompt, step.get('model', 'gpt-4.1-mini'))
            else:
                raise WorkflowError(f'Unsupported step type: {kind}')
        except KeyError as exc:
            raise WorkflowError(f'Step {name} missing required field: {exc.args[0]}') from exc
        context['steps'][name] = {'output': output}
        print(f'[OK] {name} ({kind})')
    return {'workflow': config.get('name', 'Untitled workflow'), 'steps': context['steps'],
            'output': context['steps'][name]['output']}


def load_config(path):
    with Path(path).open(encoding='utf-8') as handle:
        return json.load(handle)
