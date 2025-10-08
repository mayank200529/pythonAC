"""
Functions are the Block of codes to perform task repeteadly 

                                    ---> User Defined
There are two type of functions ---|
                                    ---> System Defined

USER DEFINED FUNCTIONS:
# def keyword is used to define functions in python
"""
def showName():             # Declaring a function
    print("Mayank Rawat")   # Task of function

showName();                 # Calling a function

"""
How many ways are there to create functions?


There are four ways to create functions :--
    1. No argue and No return value
    2. With argue and no return value
    3. With arguement and with return value
    4. No arguement and with return value
"""

# 1. No argue and No return value
# Eg-
def sum():
    a = 10
    b = 20 
    c = a + b
    print("SUM of A & B is :-",c)
sum(); # Here no arguemnet and wirtten value is given

# 2. With argue and no return value
# Eg-
def sum(a,b):
    c = a+b
    print("SUM of A & B is :-",c)
    
a = 100
b = 200
sum(a,b)
    
# 3. With arguement and with return value
# Eg-
def sum(a,b):
    c = a + b
    return c

a = 100
b = 250
c = sum(a,b)
print("Sum of A & B is -->",c)

# 4. No arguement and with return value
# Eg-
def sum():
    a = 50
    b = 90
    c = a + b
    return c

c = sum()
print("Sum of A and B is -->",c)


"""
There are 4 types of ARGUEMENTS in python functions-
|
 --> Variable Length Arguements
 --> Default Arguements
 --> Keyword Arguements
 --> Required Arguements
"""

print("\n1.Required Arguements :-")
def showData(a,b,c):
    print(a) 
    print(b) 
    print(c) 
id = 91
name = "Mayank Rawat"
city = "Ajmer"
showData(id,name,city)

print("\n2.Keyword Arguements :-")
def showData(a,b,c):
    print(a) 
    print(b) 
    print(c) 
id = 91
name = "Mayank Rawat"
city = "Ajmer"
showData(a=id,c=city,b=name)

print("\n3.Default Arguements :-")
def showData(a = "Pal",b="Rajsamand",c = "110" ):
    print(a) 
    print(b) 
    print(c)
showData()
print("\nOveriding Data : ")
id = 91
name = "Mayank Rawat"
city = "Ajmer"
showData(id,name,city)

print("\n4.Variable Length Arguements :-")
# For list or tuple
def showData(*a):
    # for i in a:
        # print(i)
    print(a)

id = 911
name = "Palllllll"
city = "Mumbai"
showData(id,name,city) 

# For dictionary 
def showData(**a):
    print(a)

id = 911
name = "Palllllll"
city = "Mumbai"
showData(a = id,b = name,c = city)  