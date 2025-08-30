# * 
# * * 
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# or jugaad
print()
for i in range(1,6):
    print("* "*i)
 
# * * * * *
# * * * *
# * * *
# * *
# *

print()
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print()
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()
# 1
# 0 1
# 1 0 1
# 0 1 0 1 
# 1 0 1 0 1
x = 1
for i in range(1,6):
    x = 0 if i % 2 == 0 else 1
    for j in range(1,i+1):
        print(x,end=" ")
        x = 0 if x == 1 else 1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
print()
x = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(x,end=" ")
        # x = (x + 1)%10
        x = x + 1 if x < 9 else 0
    print()


print()
x = 0
for i in range(1,6):
    for j in range(1,i+1):
        print(x if x <= 9 else chr(55+x),end=" ")
        x= x+1
    print()

