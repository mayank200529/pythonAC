#wap to print factorial of  a number
n1 = int(input("Enter no. for factorial- "))
x1 = 1
while n1 >= 1:
    x1 = x1 * n1
    print(f"{n1} *", end=" ")
    n1 = n1 - 1
print("\b\b=",x1)

#wap to print revrse of a number 
n2 = int(input("Enter no. for reverse- "))
x2 = 0
while n2 > 0:
    x2 = x2 * 10 + (n2 % 10)
    n2 = n2 // 10
print(x2)

#wap len or no. of digit of a number
n3 = int(input("Enter no. for length- "))
print("No of digit in no. is-",len(str(n3)))

