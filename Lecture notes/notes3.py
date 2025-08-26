"""
num = int(input("Enter a no."))
if (num % 2 == 0 and num % 7 == 0):
    print("no is even and divisible by 7")

--------------
    
user = "admin"
if user == "admin":
    print("hello admin")
elif user == "employee":
    print("hello employee")
elif user == "customer":
    print("hello customer")
else:
    print("wrong input")
----------------
num = int(input("enter a no."))

if (num >= 0 and num <=9):
    print("One digit") 
elif (num >= 10 and num <= 99):
    print("two digit") 
elif (num >= 100 and num <= 999):
    print("three digit") 
elif (num >= 1000 and num <= 9999):
    print("four digit")

-------------

"""
u = int(input("Enter units- "))
a = 0
if (u >= 0 and u <= 50):
    a = u * 2.50
elif (u >= 51 and u <= 150):
    a = 50 * 2.50 + (u - 50)*4.50
elif (u >= 250 ):
    a = 50 * 2.50 + 100 * 4.50 + (u - 150) * 6.50
else:
    a = (50 * 2.50) +(100 * 4.50) +(100 * 6.50) + (u - 250) * 8.50
print(f"total bill is ${a}")

"""
u = int(input("Enter units- "))
a = 0
if (u >= 0 and u <= 50):
    a = 0
elif (u <= 150):
    a = (u - 50)*100
elif (u >= 250 ):
    a = 100 * 100 + (u - 100) * 200
else:
    a = (100 * 100) +(100 * 200) + (u - 250) * 8.50
print(f"total bill is ${a}")


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
"""
