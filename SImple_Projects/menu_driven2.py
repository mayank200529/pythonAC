print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for exit")
d = 1
while d <= 4:
    i = int(input("Enter Choice- "))
    if i == 1:
        a = int(input("Enter first no.- "))
        b = int(input("Enter second no.- "))
        print(a + b)
    elif i == 2:
        a = int(input("Enter first no.- "))
        b = int(input("Enter second no.- "))
        print(a - b)
    elif i == 3:
        a = int(input("Enter first no.- "))
        b = int(input("Enter second no.- "))
        print(a * b)
    elif i == 4:
        a = int(input("Enter first no.- "))
        b = int(input("Enter second no.- "))
        print(a // b)
    elif i == 5:
        print("exit")
        d = 5
    else:
        print("Invalid input")

        

        
                
            