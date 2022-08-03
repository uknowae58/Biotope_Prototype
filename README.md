# PDDL API

# How to run
install waitress and flask

# Unix
Run server.py or run.sh
(In the future, one will be for debugging, the other for deployement)

# non Unix  

Since the app will be dockerized and ran under linux, windows support is partial. 


In template.py change 

template_loc, problem_loc,return_loc

in inquire.py change

jar_directory, pddl_directory, domain_directory,deff

in main.py change

return_loc

# How to Use Solver

Send the request json to the endpoint /solve. 
Example Command:

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "environment": [
        {
            "name":"o1", "value":"Berlin", "type":"ort" 
        },
        {
            "name":"t1", "type":"tisch"
        },
        {
            "name":"r1", "value":"Asia Temple", "type":"restaurant-id"
        }
    ],
    "init":[ 
        "(restaurant-ist-an-ort r1 o1)" 
    ],
    "goal":  "(and (tisch-gebucht t1) (tisch-ist-in-restaurant t1 r1)"
}
' \
  http://localhost:5000/solve


# How to query domain

/predicates takes two arguments types and match. Both are optional.

types is for searching the predicate that uses a certain type.​

Match is for choosing between exact and non exact matches about the type​

Example Command: curl 'localhost:5000/predicates?types=parkplatz-id&match=EXACT'​ ​ ​ ​

/types takes three arguments search,match,inheritence all three are optional.​

Search is for getting the keyword.​

Match is for choosing between exact an non exact matches

​Inheritance is for choosing between supertypes and subtypes

​Example Command: curl 'localhost:5000/types?search=elektroParkplatzId&match=false&inheritence=sub'​ ​ ​