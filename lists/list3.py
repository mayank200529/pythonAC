
# wap to print
# ***
# *****
# *
# ******
# ****
l = [3,5,1,6,4]
for i in l:
    print("*"*i)
print()


# wap to print
# * * * * *
# * *   * *
# * *   * *
#   *   * *
#   *   *
#       *
l = [3,5,1,6,4]
m = max(l) #here we know m = 6
for i in range(1,m+1):
    for j in range(1,len(l)+1):
        print("*" if l[j-1] >= i else " ",end=" ")
    print()

# WAP to print
#       *
#   *   *
#   *   * *
# * *   * *
# * *   * *
# * * * * *
print()
l = [3,5,1,6,4]
m = max(l) #here we know m = 6
for i in range(1,m+1):
    for j in range(1,len(l)+1):
        print("*" if (m-l[j-1] < i) else " ",end=" ")
    print()