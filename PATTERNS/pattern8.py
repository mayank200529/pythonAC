#        *       * * * * *
#        *       *
#        *       *
#        *       *
#        * * * * * * * * *
#                *       *
#                *       *
#                *       *
#        * * * * *       *
n = 5
for i in range (1,n+n):
    for j in range(1,n+n):
        print("*" if i == n or (i == 1 and j>=n) or (i == 9 and j<=n)or (i <= n and j==1)or (j == 9 and i>=n) or j == n else " ",end=" ")
    print()


print()
n = 5
for i in range (1,n+n):
    for j in range(1,n+n):
        print("*" if i == 1 or i == 9 or j ==1 or j == 9 else " ",end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#      1
#     2 2
#    3 3 3
#   4 4 4 4
#  5 5 5 5 5
print()
for i in range(1,6):
    print(" "*(5-i),end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# *
# * *
# * * *
# * * * *
# * * * * *
print()
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
print()
for i in range(1,6):
    print("  "*(5-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


print()
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

print()
n = 5
for i in range(1,n+n):
    for j in range(1,n+n):
        print("*",end=" ")
    print()


print()
for i in range(1,8):
    for j in range(1,5):
        print("*",end=" ")
    print()

print()
for i in range(1,6):
    print(" "*(i),end=" ")
    for j in range(1,6):
        print("*",end=" ")
    print()

