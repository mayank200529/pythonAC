#DAY 4 :)

#DICTIONAR IN PYTHON
# KEY:VALUE PAIRS
# dictionary is mutable
# diff key cannot have same name

# dict = {
#     "name":"mayank",   #"key":"value"
#     "learning":"python", #str
#     "age": 19,
#     "is adult": True, #boolean
#     12 : 334, #int
#     23 : 36.77, #float
#     "topics":("c++","dsa","oops"),
# }
# print(dict)
# print(type(dict))
# print(dict["name"])
# print(dict[12])
# print(dict["topics"])

# dict["name"] = "new name"  #overwrite
# dict["surname"] = "rawat" #add new key
# print(dict)

# null_dict = {}
# null_dict["name"] = ["mayank"]
# print(null_dict)

# #NESTED DICTIONARIES
# student = {
#     "name" : "Rahul kumar",
#     "subjects" : { 
#         "phy" : 45,
#         "chem" : 49,
#         "math" : 43,
#     }
# }
# print(student)
# print(student["subjects"]["chem"])


# #METHODS IN DICTIONARYY
# student = {
#     "name" : "Rahul kumar",
#     "subjects" : { 
#         "phy" : 45,
#         "chem" : 49,
#         "math" : 43,
#     }
# }
# #1 .keys()
# print(student.keys()) #returns all the keys
# print(list(student.keys())) #typecasting in list
# print(len(student)) #no. of keys

# #2 .values
# print(student.values()) #return all values
# print(list(student.values()))

# #3 .items
# print(student.items())  #return all (key,val) pairs as tuple
# print(list(student.items()))

# #4 .get("key")
# print(student.get("name2"))  #return the key acc to vaule. This show none when other than name
# # print(student["name"]) #this show error other than name so not practical
# print(list(student.get("name")))

# #5 .update(newDICT)
# new_dict = {"city":"ajmer"}
# student.update(new_dict)
#   #or
# # student.update({"city":"ajmer"})
# print(student)


# #SET in python
# # set is te collection of all unordered unique value

# collection = {1,2,3,4,"hello","world","world"}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection_1 = set()
# print(type(collection_1)) #empty set

# #methord in set
# collection = set()

# #1 .add   it adds an element
# collection.add(2)
# collection.add(3)
# collection.add("apnacollege")
# collection.add((1,2,3)) #tuple
# # collection.add({1,2,3}) #list  #this show error

# print(collection)

# #2 .remove   it removes an element
# collection.remove(3)
# print(collection)

# #3 .clear()
# collection.clear()
# print(len(collection))

# #4 .pop (it removes a random value)
# collec = {"hii","me","she","they"}
# print(collec.pop())

# #5 .union   (it combines both set values and returns new)
# set1 = {1,2,3,4}
# set2 = {3,4,6,7}
# print(set1.union(set2))

# #6 .intersection
# set1 = {1,2,3,4}
# set2 = {3,4,6,7}
# print(set1.intersection(set2))

#WAP TO STORE WORD MEANINGS
# table:"a peice of furniture","list of facts"
# cat:"a small animal"

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furnitrue","list of facts"]
}
print(dict)


#WAP TO  