#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
N = 5
for i in range(1,N+1):
    for j in range(1,N+N):
        print(" " if j<=N-i or j>=N+i else "*",end=" ")
    print()


# 1               1
# 1 2           2 1
# 1 2 3       3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3 4 5 4 3 2 1
print()
N = 5
x = 1
for i in range(1,N+1):
    for j in range(1,N+N):
        if j == N and i == N:
            print(x,end=" ")        
        elif j<=i :
            print(x,end=" ")
            x=x+1
        elif j>=N+N-i:
            x = x - 1
            print(x,end=" ")
        else:
            print(" ",end=" ")
    print()

print()
n = 5
x = 1
for i in range(1,n+n):
    print("*"*x)
    x = x+1 if i<N else x-1


print()
n = 5
x = 1
for i in range(1,n+n):
    for j in range(x):
        print(x,end="")
    print()
    x = x+1 if i<N else x-1


print()
n = 5
x = 1
for i in range(1,n+n):
    for j in range(1,x+1):
        print(j if j==1 or j==x else " ",end=" ")
    print()
    x = x+1 if i<N else x-1

print()
n = 5
x = 1
for i in range(1,n+n):
    for j in range(1,x+1):
        print(j if j==1 or j==x or i==n else " ",end=" ")
    print()
    x = x+1 if i<N else x-1

print()
n = 5
x = 1
for i in range(1,n+n):
    for j in range(1,x+1):
        print(j if j==1 or j==x or i>=n else " ",end=" ")
    print()
    x = x+1 if i<N else x-1

print()
n = 5
x = 1
for i in range(1,n+n):
    for j in range(1,x+1):
        print(j if j==1 or (x>n and j==x) or i>=n else " ",end=" ")
    print()
    x = x+1 if i<N else x-1

print()
n = 5
x = 1
for i in range(1,n+n):
    for j in range(1,x+1):
        print(j if j==1 or (i>=n and j==x) or i>=n else " ",end=" ")
    print()
    x = x+1 if i<N else x-1


print()
n = 5
x = n
s = 1
for i in range(1,n+n):
    print(" "*s,end=" ")
    for j in range(1,x+1):
        print(i,end=" ")
    print()
    x = x-1 if i<N else x+1
    s = s+1 if i<n else s-1

print()
n = 5
x = n
s = 1
for i in range(1,n+n):
    print(" "*s,end=" ")
    for j in range(1,x+1):
        print(x,end=" ")
    print()
    x = x-1 if i<N else x+1
    s = s+1 if i<n else s-1

print()
n = 5
x = n
s = 1
for i in range(1,n+n):
    print(" "*s,end=" ")
    for j in range(1,x+1):
        print(j,end=" ")
    print()
    x = x-1 if i<N else x+1
    s = s+1 if i<n else s-1

print()
n = 5
x = n
s = 1
for i in range(1,n+n):
    print(" "*s,end=" ")
    for j in range(1,x+1):
        print(s,end=" ")
    print()
    x = x-1 if i<n else x+1
    s = s+1 if i<n else s-1


print()
n = 5
x = n
s = 1
for i in range(1,n+n):
    print(" "*s,end=" ")
    for j in range(1,x+1):
        print(n+n-i,end=" ")
    print()
    x = x-1 if i<N else x+1
    s = s+1 if i<n else s-1

# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
print()
n = 5
for i in range(1,n+n):
    for j in range(1,n+n):
        print("*" if (i<=n and (j<=i or j>=n+n-i)) or (i>n and ((j <= n-(i-n)) or j>=n+(i-n))) else " ",end=" ")
    print()


print()
n = 5
for i in range(1,n+1):
    for j in range(1,n+n):
        print("*" if j<=i or j>=n+n-i else " ",end=" ")
    print()


print()
n = 5
for i in range(1,n+1):
    print(" "*i,"*" ,"  "*(4-i),"*" ,end=" ")
    print()