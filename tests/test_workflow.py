import unittest
from src.workflow import WorkflowError, render, run_workflow, load_config


class WorkflowTests(unittest.TestCase):
    def test_demo(self):
        result = run_workflow(load_config('examples/demo.json'), {'question': 'Where is my order?'})
        self.assertIn('WHERE IS MY ORDER?', result['output'])

    def test_missing_variable(self):
        with self.assertRaisesRegex(WorkflowError, 'Unknown variable'):
            render('{{input.missing}}', {'input': {}})

    def test_duplicate_id(self):
        with self.assertRaisesRegex(WorkflowError, 'Duplicate step'):
            run_workflow({'steps': [{'id': 'x', 'type': 'template', 'template': 'a'},
                                    {'id': 'x', 'type': 'template', 'template': 'b'}]})

    def test_invalid_step(self):
        with self.assertRaisesRegex(WorkflowError, 'Unsupported step'):
            run_workflow({'steps': [{'id': 'x', 'type': 'shell', 'command': 'echo hi'}]})

    def test_nested_template(self):
        self.assertEqual(render({'x': ['{{input.name}}']}, {'input': {'name': 'Sam'}}), {'x': ['Sam']})


if __name__ == '__main__':
    unittest.main()
