num = int(input("Enter a number - "))
age = int(input("Enter age -"))
p = input("Enter password - ")
n1 = int(input("Enter first number to check largest- "))
n2 = int(input("Enter second number to check largest- "))
#Q1 WAP to check if a number is +ve or -ve
if num > 0:
    print("No. is positive")
elif num < 0:
    print("No. is negative")
else:
    print("No. is zero")

#Q2 WAP to check if a number is odd or even
if num % 2 == 0:
    print("No. is even")
else:
    print("No. is odd")

#Q3 WAP to check if a person is eligible to vote or not
if age >= 18:
    print("You are eligible to vote")
elif age == 17:
    print("You will soon be eligible for vote")
elif age <= 0:
    print("Please enter valid age")
else:
    print("You are not eligible to vote")

#Q4 WAP to check the correct password
if p == "Mayank":
    print("Correct password!")
elif p == "Lokesh":
    print("Correct password!")
elif p == "Neha":
    print("Correct password!")
else:
    print("Incorrect password!!!")

#Q5 WAP to find largest of 2 no.s
if n1 > n2 :
    print(f"{n1} is greater than {n2}")
elif n1 < n2 :
    print(f"{n1} is less than {n2}")
else:
    print("first no.{n1} is equall to second no.{n2}")

