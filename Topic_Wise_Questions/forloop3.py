#   * * * 
# * * * * *
# * * * * *
# * * * * *
#   * * * 
for i in range(1,6):
    for j in range(1,6):
        if (i == 1 or i == 5) and (j == 1 or j == 5):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

print()

# *       *
# 
# 
# 
# *       * 
for i in range(1,6):
    for j in range(1,6):
        if (i == 2 or i == 3 or i == 4) and (j == 2 or j == 3 or j == 4):
            print(" ",end=" ")
        else:
            print("X",end=" ")
    print()
# diffnt methord
print()
for i in range(1,6):
    for j in range(1,6):
        if (i == 1 or i == 5) or (j == 1 or j == 5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 

print()
for i in range(1,6):
    for j in range(1,6):
        # if (i == j) or (i == 2*j) or (j == 2*i) or (i == 1 or i == 5) or (j == 1 or j == 5):
        if (i == j) or (j == 6-i) or (i == 1 or i == 5) or (j == 1 or j == 5):
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()

print()