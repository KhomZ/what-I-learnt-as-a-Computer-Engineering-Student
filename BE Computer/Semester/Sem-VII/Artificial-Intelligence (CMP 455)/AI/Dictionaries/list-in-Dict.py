# @List in dictionaries

# @Dictionaries = curly braces used in here

# hello: greeting word 

studentDict = {
    "name" : "Khom",
    "faculty" : "Computer",
    "rollNo" : 171347,
    "address" : "Pokhara",
    "girlfriend" : ["rita", "gita", "sita", "etc"]  
}

print(studentDict["girlfriend"][0])
# print(studentDict)
# output
# {'name': 'Khom', 'faculty': 'Computer', 'rollNo': 171347, 'address': 'Pokhara'}


# print(studentDict["faculty"])
# print(studentDict["facultyyyy"]) # error 

# print(studentDict.get("facultyy", "Key nai payena")) #get key error is not found

