# AI Agent Workflow Builder — Open-Source Python Automation Toolkit

A lightweight, JSON-configured **AI agent workflow builder** for developers learning **AI agent development**, **LLM integration**, and **business process automation**. Run deterministic workflows without an API key or connect an OpenAI model for AI-powered responses.

> Maintained by [AppliconSoft](https://appliconsoft.com/), a software development company. This is an educational MVP, not a production-grade autonomous agent framework.

## Features

- Sequential workflows defined in JSON
- Template variables (`{{input.question}}`, `{{steps.greeting.output}}`)
- Text transformations and optional OpenAI-powered steps
- Clear validation errors and step logs
- Python standard library only (3.10+)
- Unit tests and GitHub Actions CI

## Quick start (no API key required)

```bash
git clone https://github.com/habibmazahir786/ai-agent-workflow-builder.git
cd ai-agent-workflow-builder
python -m src.main examples/demo.json --input '{"question":"Where is my order?"}'
```

Windows PowerShell uses the same command, but quoting JSON can vary by shell. For a simple smoke test, copy the command above into a Bash-compatible terminal such as Git Bash.

Expected final output contains `CUSTOMER REQUEST: WHERE IS MY ORDER?`.

## Run the AI example (optional, paid API usage may apply)

Set your API key as an environment variable, **never commit it**.

**macOS/Linux:**

```bash
export OPENAI_API_KEY="your-key"
python -m src.main examples/ai-support.json --input '{"question":"How can I reset my password?"}'
```

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY = "your-key"
python -m src.main examples/ai-support.json --input '{\"question\":\"How can I reset my password?\"}'
```

If PowerShell quoting causes trouble, use Git Bash or create your own runner that passes a Python dictionary directly to `run_workflow`. The default model is `gpt-4.1-mini`; change it in the JSON file if necessary and verify model availability for your account.

## How it works

The engine executes steps in order and stores each output under `steps.<id>.output`.

```json
{
  "name": "Example",
  "steps": [
    {"id": "hello", "type": "template", "template": "Hello {{input.name}}"},
    {"id": "shout", "type": "uppercase", "text": "{{steps.hello.output}}"}
  ]
}
```

Supported step types: `template`, `uppercase`, `openai`. The tool does not execute arbitrary Python or shell commands from workflow files.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Limitations and security

- Workflows run sequentially; no branching, retries, persistent memory, or external tool execution.
- Treat workflow JSON as trusted configuration. Do not run untrusted workflows with sensitive environment credentials.
- Inputs are inserted into prompts; this is **not** a complete prompt-injection defense.
- OpenAI API calls transmit the prompt to an external service and may incur charges.
- Do not process sensitive customer information without appropriate controls and review.
- Do not commit `.env`, API keys, or confidential data.

## Use cases

- AI customer support prototypes
- LLM workflow experiments
- Python automation demonstrations
- Internal developer education

## About AppliconSoft

AppliconSoft develops custom software, mobile applications, and AI-powered solutions. For professional implementation and production architecture, explore AppliconSoft's [AI agent development services](https://appliconsoft.com/ai-agents/).

## Contributing

Issues and pull requests are welcome. Please include a reproduction example and run the test suite before submitting changes.

## License

[MIT](LICENSE)
