sum = 0
def enterProd(data):
    global sum
    prod = input("Enter Product: ").upper()
    if prod == "EXIT":
        print("Exiting to main menu")
        return
    if prod in data:
        quan = int(input("Enter Quantity: "))
        sum = sum + quan*(data[prod])
        print(f"{quan} {prod} is added to cart")
        print("Total Bill is ₹",sum)        
    else:
        print("Sorry this product is not available for now :(")
    enterProd(data)


def printBill(data):
    return sum

def clrBill(data):
    global sum
    sum = 0
    print("Bill Cleared")
    return sum
