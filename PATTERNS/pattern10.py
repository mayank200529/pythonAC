# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
print()
n = 5
for i in range(1,n+n):
    for j in range(1,n+n):
        print("*" if (i<=n and (j<=i or j>=n+n-i)) or (i>n and ((j <= n-(i-n)) or j>=n+(i-n))) else " ",end=" ")
    print()


# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
print()
n = 5
for i in range(1,n+1):
    for j in range(1,n+n):
        print("*" if j<=i or j>=n+n-i else " ",end=" ")
    print()

#   *          *
#    *        *
#     *      *
#      *    *
#       *  *
print()
n = 5
for i in range(1,n+1):
    print(" "*i,"*" ,"  "*(5-i),"*" ,end="")
    print()

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1
print()
n = 5
x = 1
for i in range(1,n+1):
    print("  "*(n-i),end="")
    x = 1
    for j in range (1,i+i):
        print(x,end=" ")
        x = x+1 if j<i else x-1
    print()

for i in range(1,n+1):
    print("  "*(i-1),end="")
    x = 1
    for j in range (1,n+n-(i+i)+2):
        print(x,end=" ")
        x = x+1 if j<=n-i else x-1
    print()

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1
print()
n = 5
x = 1
for i in range(1,n+n):
    x = 1
    for j in range (1,n+n):
        if (i<=n and (j>=n-i+1 and j<=n+i-1)) or (i>=n and (j>=(i-n+1) and j<= n+n-(i-n+1))):
            print(x,end=" ")
            x = x + 1 if j<n else x - 1
        else:
            print(" ",end=" ") 
    print()

# 5555555555
# 5444444445
# 5433333345
# 5432222345
# 5432112345
n = 5
for i in range(1,n+1):
    for j in range(1,n+n):
        print(n-i+1,end=" ")
    print()