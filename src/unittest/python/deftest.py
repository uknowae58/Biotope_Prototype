import sys
import unittest

# adding Folder_2 to the system path
sys.path.insert(0, '/Users/isse-tuc/IdeaProjects/simple_python_project/src/main/python')

from helloWorld import compare_any as cp

class HelloWorldTest(unittest.TestCase):
    def test_compare_any(self):
        a = cp(3,5)
        assert a==False
