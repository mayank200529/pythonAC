i = 1
while i <= 1000:
    n = i
    l = len(str(n))
    arm = 0 
    while n != 0:
        arm = arm + ((n%10)**l)
        n = n//10

    print(str(i) + " " if arm == i else "",end="")
    i = i + 1
    
    