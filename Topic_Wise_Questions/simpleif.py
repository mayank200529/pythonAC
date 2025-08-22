num = int(input("Enter a number - "))
num2 = int(input("Enter a number for even prime - "))
num1 = int(input("Enter a no. to compare - "))
C = input("Enter a character - ")
password = input("Enter the password - ")

#Q1 - WAP to check if a no. is +ve
if (num > 0):
    print("Num Is Positive")

#Q2 - WAP to check whether a num entered by user is even or odd
if (num % 2 == 0):
    print("Num is Even")
if (num % 2 != 0):
    print("Num is Odd")

#Q3 - WAP to check if a person's age is greater than or equal to 18
if (num >= 18):
    print("Eligible to vote")

#Q4 - WAP to check if a number is greater than 1
if (num2 > 1 and num2 == 2):
    print("Num is greater than 1 and is an even prime")

# #Q5 - WAP to check if a character is vowel (a,e,i,o,u)
if (C == "a","e","i","o","u"):
# if (char == "a" | char == "e" | char == "i" | char == "o" | char == "u" | ):
    print("Character is a vowel")

#Q6 - WAP to check wheter an entered character is an uppercase letter
if (ord(C) >= 65 and ord(C) <= 90):
    print("This is an uppercase letter")

#Q7 - WAP to check if a number is divisble by 5
if (num % 5 == 0):
    print("Number is divisible by 5")

#Q8 - WAP to check if a password entered by user is equal to "secret"
if (password == "secret"):
    print("Yes, the password enter by user is \"secret\"")

#Q9 - WAP to check whether the first no. is smaller than the second number
if (num < num1):
    # print("First number " + str(num) + " is smaller than the second number " + str(num1) )
    print(f"First number {num} is smaller than the second number {num}")