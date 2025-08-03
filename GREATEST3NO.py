#WAP to find greatest of 3no.s
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
if(a>=b and a>=c):
    print("The greatest no. is:",a)
elif(b>=c):
    print("The greatest no. is:",b)
else:
    print("The greatest no. is:",c)

# #my logic
# if(a>b and b>c):
#     print("The greatest no. is:",a)
# elif(b>c and c>a):
#     print("The greatest no. is:",b)
# elif(c>a and a>b):
#     print("The greatest no. is:",c)

