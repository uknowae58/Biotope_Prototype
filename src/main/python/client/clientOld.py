#It's a demo client use to check the send and recive function

import os
import json
import requests

print(os.path.abspath('.'))

class predefine_json:
    #26 As a user i want to provide the initial state and the goal state, for the calculation of a plan

    def __init__(self,name,value,environment_type,init,goal):
    # def __init__(self):
        self.name = name
        self.value = value
        self.environment_type = environment_type
        self.init = init
        self.goal = goal
    
    # def __init__(self):
    #     pass

    def __setitem__(self,name,value,environment_type,init,goal):
        pass


    def make_a_json(self):
        data_environment = {
            'name':self.name,
            'value':self.value,
            'type':self.environment_type
        }
        start = ('{\n\t\"environment\":')
        data_environment = json.dumps(data_environment)
        data_init = ("\n\t\"init\":[ \n\t\t\"%s\"\n\t]," % (init))
        data_goal = ("\n\t\"goal\":  \"%s\"" % (goal))
        end = ('\n}')
        jsonfile = start  + '[\n\t\t' +data_environment + '\n\t],' + data_init + data_goal + end
        print(jsonfile)

        with open('../server/Example/request.json','w') as f:
            f.write(jsonfile)



name = input("Input a name:")
value = input("Input value:")
print("Input a type:(available: ort,parkplatz-id,elektroParkplatzId,restaurant-id,tisch)\n")
environment_type = input()
print("Input a init Type:(available: (parkplatz-ist-an-ort ?p - parkplatz-id ?o - ort),(restaurant-ist-an-ort ?r - restaurant-id ?o - ort)\n")
init =  input()
print("Input a goal Type:(available: (parkplatz-ist-an-ort ?p - parkplatz-id ?o - ort),(restaurant-ist-an-ort ?r - restaurant-id ?o - ort)\n")
goal =  input()
object1 = predefine_json(name,value,environment_type,init,goal)
print(object1.make_a_json())



#send json to server
with open('../server/Example/request.json','r') as f:
    request=json.load(f)
print("Test recvie function:")
r = requests.post("http://127.0.0.1:5000", json=request)
print("Json send, check the console")

#get json from server
print("Test send function:")
r = requests.post("http://127.0.0.1:5000/send")
print(r.headers)
print(r.text)