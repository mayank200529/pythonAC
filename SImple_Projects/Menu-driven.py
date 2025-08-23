#Menu-Driven Program
print("Hello!\nThis program will help you to calculate area")
print("To calculate area of the any shape please enter the no. corresponding to it")
print("1.Circle\n2.Rectangle\n3.Square")
num = int(input("Enter the corresponding number - "))
if num == 1:
    rad = int(input("Enter radius of circle(in cm) - "))
    arofc = 3.14 * rad * rad
    print(f"Area of circle is {arofc}cm sq")
elif num == 2:
    len = int(input("Enter length of rectangle(in cm) - "))
    brd = int(input("Enter breadth of rectangle(in cm) - "))
    arofr = len * brd
    print(f"Area of rectangle is {arofr}cm sq")
elif num == 3:
    side = int(input("Enter side of square(in cm) - "))
    arofs = side * side
    print(f"Area of square is {arofs}cm sq")
else:
    print("Invalid input")