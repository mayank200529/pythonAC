#WAP to check if no. entered by user is odd or even

num_1 = int(input("Enter the number:"))
rem = num_1 % 2
if(rem == 0):
    print("The given number is even")
else:
    print("The given number is odd")