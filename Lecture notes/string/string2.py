"""
# Function in python
a = "Mayank Singh Rawat"
print(len(a))
print(a.lower())
print(a.upper())
print(a.title())
print(a.capitalize())
b = "      Mayank      "
print(b.strip())
print(b.rstrip())
print(b.lstrip())
print(a.replace("Mayank","BHAI"))
print(a.find("ank"))
print(a.find("hii"))
print(a.count("a"))
print(a.startswith("May"))
print(a.endswith("at"))
s = a.split(" ")
print(s)
s = "-".join(s)
print(s)
c = "JECRC"
print(c.isalnum())
print(c.isalpha())
print(c.isdigit())
print("Hii, my name is {}".format("Mayank"))
print(c.center(30,"*"))
print(c.encode())
print(c.swapcase())


d = "Python Programming"
x=""
for i in d:
    if x.find(i) != -1:
        continue
    print(i,"-- ",d.count(i))
    x=x+i
"""
# take a string and check no. of vowels available
a = input("Enter a string- ")
print("a - ",a.count("a"))
print("e - ",a.count("e"))
print("i - ",a.count("i"))
print("o - ",a.count("o"))
print("u - ",a.count("u"))
sum = a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")
print("Vowels-",sum)