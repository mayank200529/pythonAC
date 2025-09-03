# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

#   *
#   * *
#   * * *
#   * * * *
#   * * * * * 
print()
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# * * * * *
#   * * * *
#     * * *
#       * *
#         *
print()
for i in range(1,6):
    for j in range(1,6):
        print("*" if i<=j else " ",end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print()
for i in range(1,6):
    for j in range(1,6):
        print(j if i>=j else " ",end=" ")
    print()

# 1 2 3 4 5
#   2 3 4 5
#     3 4 5
#       4 5
#         5
print()
for i in range(1,6):
    for j in range(1,6):
        print(j if i<=j else " ",end=" ")
    print()


print()
x = 1
for i in range(1,6):
    for j in range(1,6):
        print( i if j == 1 or i == 5 or j==i else " ",end=" ")
    print()


print()
x = 1
for i in range(1,6):
    for j in range(1,6):
        print( j if j == 1 or i == 5 or j==i else " ",end=" ")
    print()



print()
x = 1
for i in range(1,6):
    for j in range(1,6):
        print( x if j == 1 or i == 5 or j==i else " ",end=" ")
    print()