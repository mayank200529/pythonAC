#Q1 WAP to find the largest of 3 no.s using nested if stmts
print("Q1 -WAP to find laregst of 3 no.s")
print("Ans1-")
n1 = int(input("Enter first number- "))
n2 = int(input("Enter second number- "))
n3 = int(input("Enter third number- "))
if n1 > n2:
    if n1 > n3:
        print(f"{n1} is the largest number")
    else:
        if n1 < n3:
            print(f"{n3} is the largest number")
elif n2 > n1:
        if n2 > n3:
            print(f"{n2} is the largest number")
        else:
            if n2 < n3:
                print(f"{n3} is the largest number")
elif n1 == n2 or n2 == n3 or n1 == n3 or n1 == n2 == n3:
    print("Please enter thee diffrent no.s")
"""
# There is a simple methord where we dont need to use nested if stmts
if(n1>=n2 and n1>=n3):
    print("The greatest no. is:",n1)
elif(n2>=n3):
    print("The greatest no. is:",n2)
else:
    print("The greatest no. is:",n3)
"""

# Q2 WAP to check if a person is eligile to donate blood
# Conditions -: age>18, weight>50kg
print("\n\nQ2 WAP to check if a person is eligile to donate blood")
print("Ans2-")
age = int(input("Enter age- "))
weight = int(input("Enter weight- "))
if age > 18:
    if weight > 50:
        print("You can donate blood")
    else:
        print("Underweight!!!")
else:
    print("Underage!!!")

#Q3 WAP to check whether the character entered by the useris alphabet digit or speacial
#  character. If alphabet check if it is consonant or a vowel?
print("\n\nQ3 WAP to check type of character")
print("Ans3-")
c = input("Enter any character -")
if (ord(c) >= 33 and ord(c) <= 47 ) or (ord(c) >= 58 and ord(c) <= 64) or (ord(c) >= 91 and ord(c) <= 96) or (ord(c) >= 123 and ord(c) <= 126):
    print("It is an Special Character")
elif ord(c) >= 48 and ord(c) <= 57:
    print("It is an digit")
elif (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
    if (ord(c) == 65 or ord(c) == 97 or ord(c) == 69 or ord(c) == 101 or ord(c) == 73 or ord(c) == 105 or ord(c) == 79 or ord(c) == 111 or ord(c) == 85 or ord(c) == 165):
        print("It is a vowel")
    else:
        print("It is an consonant") 

#Q4 WAP to check login credential one by one
print("\n\nWAP to login and check credentials")
print("Ans4 -")
un = input("enter username- ")
otp = int(input("enter otp"))
p = int(input("Enter pass"))
if un == "Mayank":
    if otp == "999":
        if p == "1234":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Wrong otp")        
else:
    print("Wrong username")

#Q5 WAP to check if the input angle can form a triangle
# also check if it is a right angle triangle 
print("\n\nQ5 WAP to check if the input angle can form a triangle")
print("Ans5 -")
ang1 = int(input("Enter first angle"))
ang2 = int(input("Enter second angle"))
ang3 = int(input("Enter third angle"))
sum = ang1 + ang2 + ang3
if sum == 180:
    print("Traingle can be formed")
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("Yes ,It is a right angled Triangle")
    else:
        print("No ,It is not a right angled Triangle")
else:
    print("It cannot form a Triangle")    