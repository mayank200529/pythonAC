#DAY 3 :)

# marks1 = 97.6
# marks2 = 69.4
# marks3 = 79.8
# marks4 = 89.7
# marks5 = 99.9 #this way it take too much time and many variables

# #LIST IN PYTHON
# marks=[97.6,69.4,79.8,89.7,99.9]
# print(marks)
# print(type(marks)) 
# print(marks[0])
# print(marks[1])
# print(len(marks)) #similar features as of string

# #in python we can store diff datatype values in single list
# student = ["Mayank",91,2005,"Ajmer"]
# student[0]="Yash"
# print(student[0])#strings are immutable in python
# print(student)   #lists are mutable in python
# # print(student[5]) #it will show error list index out of range


#  #LIST SLICING
# marks = [50,60,90,69,80]
# print(marks[1:4])
# print(marks[0:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])


# # METHORDS IN LIST
# list = [2,1,3]
# #1  .append(value)
# list.append(4)#it add an single element at last of list
# print(list)

# #2  .sort()
# list.sort() #sorts in ascending order
# print(list)

# #3 .sort(reverse=True)
# list.sort(reverse=True)
# print(list)

# list2 = ["apple","litchi","banana"]
# list2.sort()
# print(list2)

# #4 .reverse()
# list3 = ['a','d','e','c','f','b']
# list3.reverse()
# print(list3) #it reverse the list

# list3.sort()
# print(list3)

# #5 .insert(idx,elmt)
# list4 = [5,9,7,8]
# list4.insert(1,3) #list.insert(index,element)
# print(list4) #9 is replaced by 3

# #6 .remove(value)
# list = [4,3,1,9]
# list.remove(1) #removes the first occurance of 1
# print(list)

# #7 .pop(idx)
# list = [2,5,3,1]
# list.pop(2) #pop/removes the index 2 value i.e.3
# print(list) 


# #TUPLES IN PYTHON
# #It is built in data type that lets us create immutable sequence of value

# tup =(2,3,9,6)
# print(tup)
# print(type(tup))
# print(tup[0])
# # tup[0] = 5 (is show error as it is immutable)

# tup=()
# print(tup)

# tup=(1,)
# print(tup)
# #vs
# tup=(1)
# print(tup)#python interpret 1 as int not tuple

# #SLICING IN TUPLES
# tup = (1,3,2,4)
# print(tup[0:2])
# print(tup[1:3])
# print(tup[0:])
# print(tup[:3])

# #METHORD IN TUPLE
#  #1 .index(el)
# tup = (2,3,4,1)
# print(tup.index(4)) #returns index of first occurance

# #2 .count(el)
# tup = (3,8,4,8,1,7,8)
# print(tup.count(8)) #gives the no of times 8 is there in tuple


# #WAP to ask the user to enter names of thier 3 favourite movies & store them in a list.
# a = input("enter the first favorite movie:")
# b = input("enter the second favorite movie:")
# c = input("enter the third favorite movie:")
# list = [a,b,c]
# print(list) 
# #or 
# movies = []
# mov1 = input("enter the first favorite movie:")
# mov2 = input("enter the second favorite movie:")
# mov3 = input("enter the third favorite movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
# #or
# movies = []
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2nd movie:"))
# movies.append(input("enter 3rd movie:"))
# print(movies)  

# #WAP TO check if a list contains palindrome of elements.(hint:use copy() method)
# list1 = [1,2,3,2,1]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(list1==copy_list1):
#     print("It is palindrome of element")
# else:
#     print("not palindrome")

# #WAP to count the number of students with the "A" grade+ in following tuple
#   # ["C","D","A","A","B","B","A"]

# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))

# #store the above values in a list and sort them from "A" to "D"
# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

