import unittest
import json
import sys
sys.path.insert(1, './src/main/python/server')
import template


class MyTestCase(unittest.TestCase):
    with open('./src/main/python/server/Example/request-2.json') as request_file:
        request = json.load(request_file)
    with open('./src/main/python/server/Example/problem-2.pddl') as problem_file:
        problem = json.load(problem_file)

    problem_created = template.create_pddl(request)

    def test_template(self,problem,problem_created):
        self.assertEqual(problem, problem_created)

if __name__ == '__main__':
    unittest.main()
