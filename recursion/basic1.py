"""
RECURSION
    |--> When a function calls itself t is called recursion
    |--> FOR eg if we have to print numbers from 1 to 10
"""

# Eg-
a = 1
print("Numbers from 1 to 10-")
def printNum():
    global a
    print(a)
    a = a+1
    if a <= 10:
        printNum()

printNum()

# Eg-
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print("\nSum of 10 no.s ->",sum(10))

# Eg-
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print("\nFactorial -->",fact(5))

# Eg- 
print("\nFibonacii Series :-")
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))
    
for i in range(10):
    print(fibo(i))