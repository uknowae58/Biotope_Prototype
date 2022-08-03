import os
import json
import subprocess as sp
import unittest

import sys
sys.path.insert(1, './src/main/python/server')
import template

# with open('praktikum2022/server/Example/request-1-nocomment.json','r') as f:
#     response=json.load(f)
#     print(response)

init = "(restaurant-ist-an-ort r1 o1)"
data_init = ("\"init\":[ \n\t\"%s\"\n]," % (init))
data_goal = ("\"goal\":[ \n\t\"%s\"\n]," % (init))
# print(data_init)


#This tests the template file, almost to compeletion, It checks that a problem.pddl can be created from request 
#and compares the created file with the predefined test.json that we know for sure is good


class TestStringMethods(unittest.TestCase):
    
    def test_json(self):
        with open ('./src/main/python/server/Example/request-1-nocomment.json') as json_file:
            data = json.load(json_file)

        
        pddl_error = template.create_pddl(data)
        json_error = template.create_json(data)
        #check erros in creation
        self.assertEqual(True, json_error)
        self.assertEqual(True, pddl_error)
        with open ('./src/main/python/server/return.json') as json_file:
            actual = json.load(json_file)
        with open ('./src/main/python/server/Example/test.json') as json_file:
            test = json.load(json_file)
            
        self.assertEqual(test,actual)
        
        
        #add empty add negetive
        


if __name__ == '__main__':
    unittest.main()
