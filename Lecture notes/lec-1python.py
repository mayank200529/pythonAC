#DAY1 :)
print("my name is Mayank.","my age is 19.")
print("my age is 19.")
print("hello world")
# here print is a function
# part inside "...." is known as output
# letter in python A-Z a-z 
# digit in python 0-9
# whitespace blankspace tab 
print(23)
print(3+7)
name = "mayank"
age = 19
price = 309.98
print("my name is:",name)
print("my age is:",age)
age2 = age
print(age2)
male = True
print(male)
a = None
print(type(name),type(age),type(price),type(male))
print(type(a))
print(type(name)) 

# program to print sum of 2 no.s
a = 34
b = 26
sum = a+b
print(sum)

#arthimetic operators
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#remainder
print(a**b)#a to the power b here 5^2=25

#relational operator
a=30
b=40
print(a==b)#a is equal to b so false
print(a!=b)#a is not equal to b so true
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)

# #assignment operators
num = 10
# num = num + 10
#this statement acn also be written as
num += 10
num -= 10
num *= 5
num /= 1
num **= 10
num %= 10
print(num)
#simillarly

#logical operators
a = 50
b = 20
print(not (a>b))
print(not True)

val1 = True
val2 = False
print("AND operator:",val1 and val2)
print("OR operator:",val1 or val2)
print("and operator:",(a>b) and (a<b))

# user input
name = input("enter your name-:")
print("welcome :",name)

val = (input("enter some value:"))
print(type(val),val)#here type of value is str

val1 = int(input("enter some value:"))
print(type(val1),val1)#here type of value is int

val2 = float(input("enter some value:"))
print(type(val2),val2)#here type of value is int

name = input("enter your name:")
age = int(input("enter age:"))
marks = int(input("enter marks:"))

print("welcome:",name)
print("age =",age)
print("marks =",marks)

# write a prog to input 2 numbers and print the sum
a = int(input("enter the first no.:"))
b = int(input("enter the second no."))
sum = a + b
print("The sum of two no.s is=",sum)

#wap means write a program
#wap to input side of a square and print its area
side = float(input("enter side of square:"))
area = side*side
print("area of the square is:",area)

#WAP TO INPUT two floating point no.s & print thier average
a = float(input("first no.:"))
b = float(input("second no.:"))
print("The avg of two no.s is:",(a+b)/2)
# OR
# sum = a+b
# avg = sum/2
# print("the avg of the given numbers is:",avg)

#WAP to input 2 int no.s, a and b
#print True if a is greater than or equal to b. if not print False
a=int(input("enter value of a:"))
b=int(input("entter value of b:"))
print((a>=b))

