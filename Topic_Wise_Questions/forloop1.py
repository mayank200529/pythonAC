for i in range(1,10+1):
    print(i,end=" ")

print("\n")

for i in range(-10,0):
    print(i,end=" ")

print("\n")

n = int(input("enter no.- "))
for i in range(n,0):
    print(i)

list = [2,3,4,5,6]
for i in list:
    print(i,end=" ")

print("\n")

string = "MAYANK"
for i in string:
    print(i)

print("\n")

num = int(input("Enter no. for table-"))
for i in range(1,10+1):
    print(f"{num} * {i} = {num*i}")

print("\n")

# n = int(input("enter no. for sum"))
# for i in range(1,n+1):
#     x = x + i
#     print(x,end=" ")

n = int(input("enter no.- "))
count = 0
for i in str(n):
    count=count+1
print("no.of digit- ",count)

print("\n")

# PRINT CUBE OF NO.
n = int(input("enter no.for cube- "))
for i in range(1,n+1):
    print(i*i*i,end=" ")

print("\n")

# multiple of 5 from list
list = [2,5,10,4,36,90]
for i in list:
    if i % 5 == 0:
        print(i,end=" ")

print("\n")

for i in range(1,5+1):
    print("*"*i,end="\n")

print("\n")
list = [2,5,10,4,36,90]
for i in list:
    if i % 2 == 0:
        print(i,"even")
    else:
        print(i,"odd")    