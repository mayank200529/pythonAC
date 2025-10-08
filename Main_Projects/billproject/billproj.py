import os
import sys
import msvcrt as msv
import billmodule as bm


data = {"SHIRT":1000,"JEANS":1200,"LOWER":800,"SHOES":4500,"SOCKS":100,"SHORTS":350,"T-SHIRT":600,"TIE":250,"PANT":900,"SLIPPER":750}

def gotomain():
    print("\n1. To Clear the bill")
    print("2. To Proceed with next bill")
    print("3. To EXIT")
    print("\nEnter Your Choice:")
    ch1 = msv.getch()
    if ch1.decode() == "1":
        print("Bill Reset to: ₹",bm.clrBill(data))
        gotomain()
    if ch1.decode() == "2":
        mainUI()
    if ch1.decode() == "3":
        pass

def mainUI():
    os.system("cls")
    print("*"*10,"BILL PROJECT MADE BY MAYANK","*"*10)
    print("*"*18,"WELCOME ","*"*18,"\n\nGiven below is the product available and price :-\n")
    for i in data:
        print("Product:",i," ","Price: ",data[i])

    print("\n1. Add an item to bill ")
    print("2. Get the total bill")
    print("3. Clear Bill")
    print("4. Exit")
    print("\nEnter Your Choice:")
    ch = msv.getch()
    if ch.decode() == "1":
        print(bm.enterProd(data))
        mainUI()
    if ch.decode() == "2":
        print("Your bill is: ₹",bm.printBill(data))
        gotomain()
    if ch.decode() == "3":
        print("Bill Reset to: ₹",bm.clrBill(data))
        gotomain()
    if ch.decode() == "4":
        pass
mainUI()