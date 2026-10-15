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

[AppliconSoft](https://appliconsoft.com/) is a software development company specializing in artificial intelligence, AI agent development, business automation, custom software engineering, and mobile and web application development.

We help businesses design, develop, and deploy scalable digital solutions that improve operational efficiency, automate workflows, and support digital transformation.

This open-source **AI Agent Workflow Builder** is maintained by AppliconSoft to help developers explore AI agent development, intelligent automation, and modern software engineering practices.

## Our Services

AppliconSoft offers end-to-end software development, artificial intelligence, automation, and digital transformation services.

### Artificial Intelligence & Automation

- **[AI Agent Development Services](https://appliconsoft.com/ai-agents/)** — Custom AI agents, intelligent assistants, and automated business workflows.
- **[AI, Automation & Data Science](https://appliconsoft.com/service/ai-automation-data-science/)** — AI-powered solutions, machine learning, data analytics, and intelligent process automation.

### Software & Application Development

- **[Custom Software & Backend Development](https://appliconsoft.com/service/custom-software-backend-development/)** — Scalable custom software, backend systems, APIs, and enterprise applications.
- **[Website & Web Application Development](https://appliconsoft.com/service/website-web-application-development/)** — Responsive websites, custom web applications, dashboards, and online platforms.
- **[Mobile App Development Services](https://appliconsoft.com/service/mobile-app-development/)** — Native and cross-platform mobile applications for Android and iOS.
- **[UI/UX Design & Front-End Engineering](https://appliconsoft.com/service/ui-ux-design-front-end-engineering/)** — User-centered interfaces, responsive designs, and modern frontend development.

### Business Solutions & Consulting

- **[CRM, ERP & Business Automation](https://appliconsoft.com/service/crm-erp-business-automation/)** — CRM and ERP customization, system integrations, and business workflow automation.
- **[Business Analysis & IT Consultancy](https://appliconsoft.com/service/business-analysis-it-consultancy/)** — Requirements analysis, IT consulting, solution architecture, and technology planning.
- **[Software Quality Assurance & Testing](https://appliconsoft.com/service/software-quality-assurance-testing/)** — Functional testing, regression testing, quality assurance, and software validation.

### Digital Platforms & Emerging Technologies

- **[E-Commerce Development](https://appliconsoft.com/service/e-commerce-development/)** — Custom online stores, e-commerce platforms, and payment gateway integrations.
- **[CMS Development](https://appliconsoft.com/service/cms-development/)** — Content management systems, custom themes, plugins, and CMS integrations.
- **[Blockchain Development](https://appliconsoft.com/service/blockchain-development/)** — Blockchain applications, smart contracts, and decentralized solutions.
- **[Digital Growth & SEO Services](https://appliconsoft.com/service/digital-growth-seo-services/)** — Technical SEO, search visibility optimization, website performance, and digital growth strategies.

## Why Choose AppliconSoft?

AppliconSoft combines software engineering expertise with modern AI and automation technologies to help businesses build reliable, scalable digital solutions.

Whether you need a custom AI agent, enterprise automation, mobile application, or complete software platform, our team can help turn your requirements into practical solutions.

**Explore all services:** [AppliconSoft Software Development Services](https://appliconsoft.com/services/)

## Contributing

Issues and pull requests are welcome. Please include a reproduction example and run the test suite before submitting changes.

## License

[MIT](LICENSE)
