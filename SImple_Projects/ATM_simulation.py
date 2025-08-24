#ATM Simulation
"""
concept-- ask for pin check if correct,
check if amt <= balance,
then allow withdrawl ,
else show "insufficent balance"
"""
pin = int(input("Enter pin - "))
bal = 10000
if pin == 9999:
    amt = int(input("Enter amount- "))
    if amt <= bal:
        print(f"Withdrawl of ₹{amt} is successful")
    else:
        print("Insufficient Balance!!!")
else:
    print("Incorrect pin!!!")