import json
from math import fabs
from flask import Flask, jsonify, request, render_template, request,Blueprint

# app = Flask(__name__)
#Use Blueprint to connect with main
bp = Blueprint('bp', __name__, template_folder='templates')

@bp.route('/')
def index():
  return render_template('home.html')

@bp.route('/result',methods = ['POST','GET'])
#TODO get response.json and show in webpage
#TODO after got response, delete request.json and response.json in server
def result():
    if request.method == 'POST':
        result = request.form

        dictresult = result.to_dict()
        pddlEnvironmentName = dictresult['name']
        pddlEnvironmentValue = dictresult['value']
        pddlEnvironmentType = dictresult['type']

        pddlInit = dictresult['predicates type']
        # Indeveloping function
        # pddlGoal = searchGoal(pddlInit)
        pddlGoal = '(restaurant-id)'

        #convert type to independent dictory and combination name value and type into 1 dictory
        pddlEnvironmentdict = {'name':pddlEnvironmentName,'value':pddlEnvironmentValue,'type':pddlEnvironmentType}
        pddlInitdict = {'init':pddlInit}
        pddlGoaldict = {'goal':pddlGoal}
        #convert dictory to list
        pddlEnvironmentlist = []
        pddlEnvironmentlist.append(pddlEnvironmentdict)
        pddlInitlist = []
        pddlInitlist.append(pddlGoaldict)
        pddlGoallist = []
        pddlGoallist.append(pddlGoaldict)

        #make dictory suit with PDDL
        pddlJson = {'enviroment':pddlEnvironmentlist,'init':pddlInitlist,'goal':pddlGoallist}

        #Convert the input result to json
        json_str = json.dumps(pddlJson,sort_keys=False,indent=4)
        jsonGenerate(json_str)

        return render_template('result.html',result = result,data = json_str)

def jsonGenerate(result):
    #generate JSON file and save
    with open("request.json", "w", encoding='utf-8') as outfile:
        outfile.write(result)

#TODO Search domain.pddl for goal
def searchGoal(pddlInit):
    pass

if __name__ =="__main__":
  # didn't find how to access waitress server from WAN, so use default Flask WSGI server instead
  app.run(debug=True,host="0.0.0.0",port=5000)