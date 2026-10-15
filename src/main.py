"""CLI entry point: python -m src.main examples/demo.json --input '{...}'"""
import argparse
import json
import sys
from .workflow import WorkflowError, load_config, run_workflow


def main():
    parser = argparse.ArgumentParser(description='Run a JSON-configured AI agent workflow')
    parser.add_argument('workflow', help='Path to workflow JSON')
    parser.add_argument('--input', default='{}', help='Input JSON object')
    args = parser.parse_args()
    try:
        inputs = json.loads(args.input)
        if not isinstance(inputs, dict):
            raise WorkflowError('--input must be a JSON object')
        result = run_workflow(load_config(args.workflow), inputs)
        print('\n' + json.dumps(result, indent=2, ensure_ascii=False))
    except (WorkflowError, OSError, json.JSONDecodeError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
