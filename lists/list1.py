# declare list methord 1
l = []
print(type(l))

# declare list methord 2
l = list()
print(type(l))

# eg 
list1 = [1,2,5,6]
list2 = ["a","b","c",4,6,7,8]
list3 = [1,"s",6,9,True,"d"]
print(list1)
print(list2)
print(list3)

# conversion of string in list
a = "Mayank"
l = list(a)
print(l)


l1 = ["ajay","rahul","Mayank","pal","Neha"]

print(l1)
print(l1[2])

for i in l1:
    print(i,end=" ")
print()

for i in range(len(l1)):
    print(l1[i],end=" ")

# string is mutable
print()
print(l1)
l1[2]="Mukul"
print(l1)
