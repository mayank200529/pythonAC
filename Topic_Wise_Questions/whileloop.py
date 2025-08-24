"""
#Print the following PATTERNS

#1 - 1 2 3 4 5 6 7 8 9 10
x = 1
while x <= 10:
    print(x , end = "  ")
    x = x + 1 

print("\n")

#2 - Sum of Natural no.s 
a = 1 
s = 0
while a <= N:
    print(a , end = " + ") 
    s = s + a
    a = a + 1
print("\b\b=",s)

print("\n")

#3 sum of N natural no.s
N = int(input("Enter N- "))
a = 1 
s = 0
while a <= N:
    print(a , end = " + ") 
    s = s + a
    a = a + 1
print("\b\b=",s)

print("\n")

#4 Multiplication table
tab = int(input("Enter the number to get multiplication table- "))
n = 1
print(f"Multiplication Table of {tab}:-")
while n <= 10:
    mult = tab * n
    print(f"{tab} * {n} = {mult}" , end="\n")
    n = n + 1

#5 Sum of digit of a number
n = int(input("Enter a numer - "))
s = 0
while n>0:
    print(n%10)
    s = s + (n%10)
    n = n // 10
print(f"The sum of the digits is {s}")    

#6 Count the digit in number
b = int(input("Enter a number- "))
count = 0
while b>0:
    digit = b % 10
    b = b // 10
    count = count + 1
print(count)
"""
#7 Reverse of a number
number = int(input("Enter any number - "))
while number>0:
    digit = number % 10
    number = number // 10
    print(digit)