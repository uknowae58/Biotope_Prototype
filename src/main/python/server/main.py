import os
from re import template
import subprocess as sp
import json 
from flask import Flask, jsonify, request, render_template
import string
import inquire
import template

from waitress import serve
import template

#connect with client
from client import bp


#to run server set environment variable FLASK_APP to hello.py
app = Flask(__name__)
app.register_blueprint(bp)
return_loc= './src/main/python/server/return.json'
input = []

@app.route('/predicates')
def send_predicate():
  types = request.args.get('types')
  match = request.args.get('match')
  return inquire.get_predicate(types,match)


@app.route('/types')
def send_type():
  search = request.args.get('search')
  match = request.args.get('match')
  inheritence = request.args.get('inheritence')
  return inquire.get_type(search,match,inheritence)



#us:19 send json not connected 
#todo make it send our json files for test, response-1.json.

#send after recive

@app.route('/send',methods=['POST'])
def send_json():
  with open('./server/Example/response-1.json','r') as f:
    response=json.load(f)
  return jsonify(response)



#us:20 receive json

@app.route( '/receive', methods=['POST'])
def receive():
  input=request.get_json()
  print(input)
  return "Json received",204



@app.route('/solve', methods=['POST'])
def main():
  input=request.get_json()
  
  
  #US 61 HERE 
  
  error = template.confirm_request(input)
  if error != None:
    return error
  
  
  pddl_result = template.create_pddl(input)
  json_result = template.create_json(input)
  if json_result !=True:
    return json_result
  if pddl_result !=True:
    return pddl_result
  with open(return_loc,'r') as f:
  #There is a problem that json file not allow any comment
    result=json.load(f)
  return jsonify(result)




if __name__ =="__main__":
  #  from waitress import serve
  #  serve(app, host="0.0.0.0", port=5000)
  # didn't find how to access waitress server from WAN, so use default Flask WSGI server instead
  app.run(debug=True,host="0.0.0.0",port=5000)

