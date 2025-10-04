d = {"Rno.":"101","name":"Mayank Rawat","age":"20","hindi":40,"english":50}
print(d)

print("name" in d.keys())

# WAP to print all keys in dict
print("\nKEYS")
for i in d.keys():
    print(i)
# WAP to print all VALUEs in dict
print("\nVALUES")
for i in d.values():
    print(i)
# WAP to print all items in dict
print("\nITEMS")
for i in d.items():
    print(i)

# WAP to merge two dict
print("\nMerge Two Dictionary")
d1 = {"Mayank":"Rawat","Pal":"Chaplot","Neha":"Dhakar"}
d2 = {20:"Maths",45:"English","Lokesh":"Saini"}
d1.update(d2)
print(d1)

print("\n")
# Create a dict of 5 student where key = roll no,value=name  print all ROLL NO.
student = {1:"Mayank",2:"Neha",3:"Pal",4:"Nishita",5:"Lokesh"}
print(student)
print("\nRoll no.s of 5 stdents-")
print(student.keys())
for r in student.keys():
    print(r)
print()
print(student.values())
for r in student.values():
    print(r)
print()
print(student.items())
for r in student.items():
    print(r)
# or
print()
key = [101,102,103,104,105]
value = ["Mayank","Pal","Neha","Lokesh","Nishita"]
d = {"Key":key , "value":value}
print(d)




