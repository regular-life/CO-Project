from utils.Helper import *
from data.Error import *

import sys

document = []
current_sentence = []
line_list = sys.stdin.readlines()
for line in line_list:
    current_sentence = line.strip().split()
    document.append(current_sentence)
#with open("input.txt", "r") as f:
 #   for line in f:
  #      current_sentence = line.strip().split()
   #     document.append(current_sentence)

no_of_sentence = len(document)

# Finding Labels

no_of_variable = 0
no_of_label = 100
line_1 = 0
x = -1
y = 0
var_check = True
for i in range(no_of_sentence):
    if not document[i]:
        pass
    else:
        if document[i][0] == "var":
            if not var_check:
                print(Error_Code[107],"at line",i+1)
                exit()
            elif document[i][-1] in variable_store or document[i][-1] in label_store:
                print(Error_Code[106],"at line",i+1)
                exit()
            else:
                variable_store[document[i][-1]] = [no_of_variable, -1]
                no_of_variable = no_of_variable + 1
        else:
            var_check = False
            y+=1
        if document[i][0][-1] == ":":
            if document[i][0][:-1] in label_store or document[i][0][:-1] in variable_store:
                print(Error_Code[106],"at line",i+1)
                exit()
            else:
                label_store[document[i][0][:-1]] = [y-1, x]
                no_of_label = no_of_label + 1
                document[i] = document[i][1:]

for i in variable_store:
    variable_store[i][0] += y
line = 0

for i in range(no_of_sentence):
    if not document[i]:
        pass
    elif document[i][0] == "var":
        pass
    else:
        if document[i][0] == "mov":
            if document[i][-1][0] == "$":
                document[i][0] = "movi"
            else:
                document[i][0] = "movr"
        a = Shelf(document[i])
        if a.error == 404:
            Shelf.lines.append(a)
        else:
            print(Error_Code[a.error],"at line",line+1)
            exit()
    line += 1

temp = 0
for i in Shelf.lines:
    if i.name == "hlt":
        temp+=1
        
if(temp<1):
    print(Error_Code[108])
    exit()
    
elif temp>1:
    print(Error_Code[111])
    exit()
    
if Shelf.lines[-1].name != "hlt":
    print(Error_Code[109])
    exit()

if len(Shelf.lines) + len(variable_store) >128:
    print(Error_Code[100])
    exit()

# with open("output.txt","w") as f:
for i in Shelf.lines:
    print(i.bin)
