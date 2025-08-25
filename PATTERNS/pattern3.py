"""
#print reverse counting in decreasing order upto 0
x = int(input("Number = "))
while (x >= 0):
    print(x,end=" ")
    x = x - 1

print("\n ")

#print counting from 0 to a number
x1 = int(input("Number = "))
n = 0
while n <= x1:
    print(n , end=" ")
    n = n + 1

print("\n ")
"""
#print factors of a number
a = int(input("enter no. to get factors-"))
n = 1
while a>0:
    if a // n == 0:
        print(n , end=" ")
    n = n + 1

