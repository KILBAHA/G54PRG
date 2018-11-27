"""
Playing with zip funciton
"""

dict = {"a": 2, "b": 3}

List = [5,6]  

for key,value in zip(dict, List):

    dict[key] = value

print (dict)

"""
Making both T and F
"""

dict = {"x":True, "y":False}

print("before{}".format(dict))

List = [False, False]
 

def changeval():
    for key,value in zip(dict, List):
        dict[key] = value

changeval()
changeval()
    
print("after{}".format(dict))


def istauto():
    for key,value in zip(dict,List):
        dict[key] = True
        
        