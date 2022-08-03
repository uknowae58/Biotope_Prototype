import json
import main

from string import Template

import inquire

template_loc = './src/main/python/templates.txt'
problem_loc = './src/main/python/problem.pddl'
return_loc = './src/main/python/server/return.json'
returnjson = {}

#for later maybe pass only the json.load object isntead of location so it can truely be restful
def create_json(data,plan=inquire.solve()):
    if 'ERROR' in plan[0:10]:
        return plan   
    returnjson = {x:data[x] for x in data if x == 'environment'}
    returnjson['composition']= []

    for steps in plan:
        temp = steps[steps.find('(')+1:steps.rfind(')')]
        step = temp.split(' ')


        params=[]
        for para in step[1:]:
            params.append(para)
        
        returnjson['composition'].append({"name":step[0],"params":params})
        
    
    
    json_object = json.dumps(returnjson, indent = 4) 
    with open(return_loc, "w") as outfile:
        json.dump(returnjson, outfile)
    return True
     
"""     for a in returnjson:
        for x in returnjson[a]:

            print (x)
            print(type(x))
         """
         
         
def create_pddl(result):
    
    #doesnt return anything,save problem.pddl to disk、
#   with open('./request.json', 'r', encoding='utf-8') as f:

#     result=json.load(f)

    objectlist = {}
    pddlEnvironment = result['environment']
    for pddlElements in pddlEnvironment:

        pddlElement = pddlElements
        objectname = pddlElement['name']
        objecttype = pddlElement['type']
        objectlist[objectname] = objecttype

    tmp_init = result['init']
    tmp_init = tmp_init[0]
    tmp_goal = result['goal']
    try:
        return make_pddl(result,object=objectlist,pddlInit=tmp_init,goal=tmp_goal)
    except:
        if "environment" not in input.keys() or "init" not in input.keys() or "goal" not in input.keys():
            return "INCORRECT JSON HAS BEEN SENT. MAKE SURE IT HAS ENVIRONMENT, INIT AND GOAL"
        if type(input["init"]) != list:
            return "[Init Error] init does not have list structure"
        if type(input["environment"]) != list:
            return "[Enviroment Error] environment does not have list structure"
        for environment in input['environment']:
            if "name" not in environment.keys() or "type" not in environment.keys():
                return "[Enviroment Error] is missing a name or a type"
        if input['init'][0][0] != '(' and input['init'][0][-1] != ')':
            return "[Init Error] init file is missing parenthesis"
        if input['goal'][0] != '(' and input['goal'][-1] != ')':
            return "[Goal Error] file is missing parenthesis"

def make_pddl(result,problemName='demoName',domain='demoDomain',object={'None':'None'},pddlInit='',goal=''):
    objectlist = ''
    for pItemList in object.items():
        pddlCombinate = '%s - %s'%(pItemList[0],pItemList[1]) + '\n'
        objectlist = objectlist + pddlCombinate


    d = {
    'problem':problemName,
    'Domain':domain,
    'objectslist':objectlist,
    'initlist':pddlInit,
    'goal': goal + ')'
    }

    with open(template_loc, 'r') as f:
        src = Template(f.read())
        result = src.substitute(d)
        print(result)

    with open(problem_loc, 'w', encoding='utf-8') as f:
        f.write(result)
    return True
