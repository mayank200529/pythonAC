d = {1:"Mayank",2:"Neha",3:"Pal",4:"Nishita",5:"Lokesh"}
print("Length of dictionary-",len(d))


d = {"Mango":"$200","Apple":"$400","Grapes":"$270","Kiwi":"$810","Banana":"$170"}
x = input("Enter Name of fruit-").title()
for i in d:
    if i == x :
        print(x,"->",d[x])

