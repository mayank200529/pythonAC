i = 1000
d = 0
w = 0
while i > 0:
    print(f"\nBalance = ₹{i}")
    print("Press 1 to deposit")
    print("Press 2 to withdraw")
    print("Press 3 to exit")
    c = int(input("\nEnter choice- "))
    if c == 1:
        dep_amt = int(input("\nEnter amount to deposit- ₹"))
        i = i + dep_amt
    elif c == 2:
        with_amt = int(input("\nEnter amount to withdraw- ₹"))
        i = i - with_amt
    elif c == 3:
        print("\nEXIT")
        i = 0
    else:
        print("\nInvalid Input")
    
