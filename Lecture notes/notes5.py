"""# check if a number is palindrome or not

x = 1 
s = 0
while x <= 5:
    s = s * 10 + x 
    print(s , end="\n")
    x = x + 1

print("\n\n")
x = 1 
s = 0
while x <= 5:
    s = s * 10 + x 
    print(s , end="\n")
    x = x + 1

# """
# #print 5*5*5 = 125
# n = 5
# p = 3
# x = 1
# while p>=1:
#     x = x * n
#     p = p - 1
# # print(f" {n}*{n}*{n} = "x)


# print(n[-1::-1])

# x = ""
# while n > 0:
#     x =   x + str(n%10)
#     n = n // 10
# print(x)



# r = 0

# while n > 0:
#     r = r * 10 + (n % 10)
#     n = n // 10
    
# print(r)

n = 1
while n <= 10000:
    i = 2
    c = 0
    while i <= n:
        if  n % i == 0:
            c = c + 1
        i = i + 1
    print ((str(n) + " ") if c == 1 else "", end="")
    n = n + 1