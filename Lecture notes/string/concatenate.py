"""
a = "mayank"
# a = a + " Rawat"
# print(a)
# a = a * 5
# print()
# print(a)

for i in a:
    # print(i,"-- ",ord(i.upper())-64)
    x=ord(i.lower())-96
    print()
    print(i,"-- ",x,"."*(x-1),"*")
    # print(i,"--",chr(65))

"""

a = "mayank"
b = "rawat"
print(a+" "+b)

a = "Mayank Rawat"
for i in a:
    x=ord(i.upper())-64
    y=97 if i.islower() == True else 65
    print(i,"-- ",x," - ",end="")
    for i in range(x):
        print(chr(y+i),end=" " )
    print()