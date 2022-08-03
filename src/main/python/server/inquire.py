
import subprocess as sp
import string


#UNIX Only
jar_directory = './src/main/python/server/Example/enhsp-dist/enhsp.jar'
pddl_directory = './src/main/python/'
domain_directory = './src/main/python/server/Example/domain.pddl'
#Windows Only
#Missing

deff=sp.getoutput('java -jar ./src/main/python/server/Example/enhsp-dist/enhsp.jar -f ./src/main/python/problem.pddl -o ./src/main/python/server/Example/domain.pddl')
#change input for dos
def solve(output=deff):
  error = str(output)
  output= str(output).splitlines()
  answers = []
  listen = False

  for line in output:
    if line=='Plan-Length:' + str(len(answers)):
        listen = False
    if listen == True:
        answers.append(line)
    if line=='Problem Solved':
        listen = True
  if len(answers)==0:
    return 'ERROR'+error
  return answers
 
 
 
input = []


def inquire():
  f = open(domain_directory,'r')
  types = []
  predicates = ''
  t=0
  p=0
  for line in f:
    #line = line.translate({ord(c): None for c in string.whitespace})
    line=line.lstrip()
    line=line.rstrip()


    if t>0 and t!=2:
      if line==')':
        if t==1: t=0

    if p>0 and p!=2:
      if line==')':
        if p==1: p=0

    if t>0 and t!=2:
        types.append(line)
    if p>0 and p!=2:
        predicates=predicates+line+'\n'


    if line=='(:types':
      t=1

    if line=='(:predicates':
      p=1


  return types,predicates


def get_predicate(types,match):
  temp=""
  garbage,predicates= inquire()

  if (types==None):
    return predicates
  else:
    typel = predicates.split('\n')
    for line in typel:
      line_types = line[line.find(' - ')+1:line.rfind(')')+1]
      if types in line_types:
        #check if trail is - and the tail is not a letter to eliminate partial matches.
        beginning = line_types[line_types.find(types)-1]
        trail = line_types[line_types.find(types)+len(types)]
        if line_types[line_types.find(types)-1]==" " and line_types[line_types.find(types)+len(types)].isalpha()==False:
          temp=temp+"Predicate \""+line[1:line.find('?')] +"\" uses these types: " + line_types.replace("?",", ")[0:len(line_types)]+ "\n"
        else:
           if match == 'false' or match == 'False':
            temp=temp+"Partial match for \"" +types+ "\" were found in predicate \""+line[1:line.find('?')] +"\" for these types: " + line_types.replace("?",", ")[0:len(line_types)]+ "\n"

    if temp=="":
      return "Given type \""+types+"\" has not been found in the domain please try again with a different argument"
    else:
      return temp
  
  
def get_type(search,match,inheritence):
  types,garbage= inquire()

  supertypes =[]
  dict = {}
  ogdict = {}
  out= ''
  for type in types:
    current = type.split(" - ")
    dict.update({current[0]:[current[1]]})
    ogdict.update({current[0]:[current[1]]})

    
    
#get subtypes until object is reached
  order = False
  while order == False:
    order = True
    for object_names in dict:
      if 'object' not in dict[object_names]:
        order == False
        dict[object_names]+=dict[dict[object_names][-1]]
        print (dict[object_names])

#check if the given type is subtype to find the supertype

  if match == None or match.upper()=='EXACT':
    for object_names in dict:
      if search in dict[object_names]:
        supertypes.append('\'\n\''+object_names+'\' inherits from \'' + search)
          
          
          
#check if the given type is subtype to find the supertype but without exact matches

  else:
    order = False
    for object_names in dict:
        for notexacts in dict[object_names]:
            if search in notexacts:
                supertypes.append('\n\''+object_names+'\' inherits from \'' + search+'\' (\''+search+'\')')

    if inheritence is not None and inheritence.upper()== 'SUPER':

      for object_names in supertypes:
        out += object_names

      if out=="":
        return "Given type \""+search+"\" has not been found in the domain please try again with a different argument"
      
      return out


  if match==None or match.upper()=='EXACT' or search in dict:
    if search in dict:
      out = 'Found an exact match for \''+search+'\' it has type \''+ ogdict[search][0] + ' \''
      if inheritence is not None and inheritence.upper()== 'SUB':
        out += 'Subtypes according to hierarchy'
        for object_names in dict[search]:
          out += '\n ->' + object_names 

  else:
    for object_names in dict:
      if search in object_names:
        out += 'found a not exact match for \''+search+'\' as \'' + object_names+'\'it has type\''+ ogdict[object_names][0] + '\''
        if inheritence is not None and inheritence.upper()== 'SUB':
          out += '\nListing subtypes according to hierarchy'

          for x in dict[object_names]:
            out += '\n ->' + x 
          
  if search == None and inheritence is not None and inheritence.upper()=='SUB':
    return jsonify(dict)
  
  if search == None and inheritence== None:
    return jsonify(ogdict)
  
  
  
  if out=="":
    return "Given type \""+search+"\" has not been found in the domain please try again with a different argument"


  return out