#wap to print 
# 1
# 21
# 321
# 4321
# 54321
print("pattern1:- ")
i = 1
x = 1
n = 0
while i <= 5:
    n = i*x + n
    print(n)
    x = x * 10
    i = i + 1

#wap to print 
#    1
#   21
#  321
# 4321
#54321
print("\npattern2:- ")
i = 1
x = 1
n = 0
while i <= 5:
    n = i*x + n
    print((" "* (5-i)),n)
    x = x * 10
    i = i + 1

# print 5*5*5
n = 5
p = 3
x = 1
print("\n")
while p >= 1:
    x = x * n
    print(f"{n} *",end = " " )
    p = p - 1

print("\b\b=",x)

# print to check if a no. is prime 
n = int(input("\nEnter no. to check for prime- "))
i = 2
c = 0
while i <= n:
    if n % i == 0:
        c = c + 1
    i = i + 1
print("Prime " if c == 1 else "Not prime")
