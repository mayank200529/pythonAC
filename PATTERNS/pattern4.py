# WAP to print 1 2 3 4 5 whne n = 5
n = 5 
x = 4
while x >= 0:
    c = n - x
    print(c,end=" ")
    x = x - 1
print("\n")

# WAP to print 5 3 1 2 4 whne n = 5
n = 5
x = 0
c = 3
while x <= 4:
    print(n - x,end=" ")
    x = x + 2
    if x > 4:    
        print(n - c,end=" ")
        c = c - 2

print("\n")

# WAP to print      *
#                   **
#                   ***
#                   ****
#                   *****
i = 1
c = 1
while i <= 5:
    print("*"*c,end="\n")
    i = i + 1
    c = c + 1


 