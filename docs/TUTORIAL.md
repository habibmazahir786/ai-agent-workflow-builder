# Build a Python AI agent workflow with JSON

A small workflow is easier to understand when each step has one job. In this tutorial, you will turn a customer question into a labeled support request using AppliconSoft's AI Agent Workflow Builder. The first example runs locally without an API key, so you can inspect how data moves before adding a language model.

## Prepare the project

Install Python 3.10 or later and download the [AI Agent Workflow Builder repository](https://github.com/habibmazahir786/ai-agent-workflow-builder), then open a terminal in the extracted `ai-agent-workflow-builder` directory. No third-party Python packages are needed for the deterministic example.

Run the included checks:

```bash
python -m unittest discover -s tests -v
```

## Define three steps

The included `examples/demo.json` contains this workflow:

```json
{
  "name": "Customer Support Demo (No API Key)",
  "steps": [
    {"id": "greeting", "type": "template", "template": "Customer request: {{input.question}}"},
    {"id": "label", "type": "uppercase", "text": "{{steps.greeting.output}}"},
    {"id": "reply", "type": "template", "template": "Support workflow processed: {{steps.label.output}}"}
  ]
}
```

The first step inserts the supplied question. The second reads the first step's output and converts it to uppercase. The third adds a prefix to produce the final message. Step IDs provide names for the outputs, and steps can reference only inputs or outputs already available when they run.

## Run a customer question

In Bash or Git Bash, run:

```bash
python -m src.main examples/demo.json --input '{"question":"Where is my order?"}'
```

The CLI prints a completion line for each step, then a JSON result. Its final `output` value should be:

```text
Support workflow processed: CUSTOMER REQUEST: WHERE IS MY ORDER?
```

If your PowerShell version changes the JSON quoting, pass a dictionary directly through Python instead:

```python
from src.workflow import load_config, run_workflow

result = run_workflow(
    load_config("examples/demo.json"),
    {"question": "Where is my order?"},
)
print(result["output"])
```

Save this as `try_workflow.py` in the project directory and run `python try_workflow.py`.

## Experiment with the data flow

Change the `reply` template to read `{{steps.greeting.output}}` instead of `{{steps.label.output}}`. The final message will retain the question's original capitalization, although the uppercase step still runs. This illustrates an important property: execution follows the order in the JSON list, while each template decides which previous output it uses.

Try referencing `{{steps.missing.output}}`. The engine reports an unknown variable instead of silently substituting an empty string. A duplicate step ID also produces a validation error. These checks make configuration mistakes easier to locate.

## Add a language model when needed

The repository also includes `examples/ai-support.json`, which uses an `openai` step. Follow the README's environment-variable instructions to set `OPENAI_API_KEY`, then run that example with a sample question. Keep the key outside workflow files and version control. Model calls send prompts to an external service and can incur charges.

Use deterministic steps for formatting and an LLM step for a task that needs language generation. Evaluate generated replies against realistic questions before using them with customers. This engine does not provide branching, retries, persistent memory, retrieval, or human handoff; those require additional implementation.

## Explore the source

Read `src/workflow.py` alongside the tests to understand variable rendering, validation, and sequential execution. Start with synthetic questions and extend one behavior at a time.

For help designing a production system, explore AppliconSoft's [AI agent development services](https://appliconsoft.com/ai-agents/).
