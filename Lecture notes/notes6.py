# n1 = int(input("Enter no 1- "))
# n2 = int(input("Enter no 2- "))
# m = n1 if n1 < n2 else n2
# gcd = 0
# for i in range(1,m+1):
#     if n1 % i == 0 and n2 % i == 0:
#         gcd = i
# print(gcd)

n = 1234
x = ""
for i in str(n):
    x = x + i
    print(x,end=" ")