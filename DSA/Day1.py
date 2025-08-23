# Question 1
# add digits of a number 
n = 452
a = n % 10
n = n // 10
b = n % 10
n = n // 10
c = n
print(a+b+c)

n = 452
a = (n%10) + (n//10)%10 + (n // 100)
print(a)

# Question 2
# reverse of a number 
n = 452
a = (n % 10)*100 + ((n // 10)%10) * 10 + (n // 100)
print(a)

#question 3
# swap two numbers 
a = 5
b = 4

temp = a
a = b
b = temp

print(a)
print(b)


# Question 1
# swap two no.s 
# 5 ways

# first (3rd variable)
print("methord 1")
a = 10
b = 20
print(a ," ",b)
temp = a
a = b
b = temp
print(a ," ",b)

# second (add and subt)
print("methord 2")
a = 10
b = 20
print(a ," ",b)
a = a + b
b = a - b
a = a - b
print(a ," ",b)

# third (div and mult)
print("methord 3")
a = 160
b = 140
print(a ," ",b)
a = a * b
b = a // b
a = a // b
print(a ," ",b)

# fourth (pyhton trick)
print("methord 4")
a = 50
b = 60
print(a ," ",b)
a,b = b,a
print(a ," ",b)


print("methord 5")# fifth (BITWISE  XOR(^) )


a = 30
b = 20
print(a ," ",b)
a = a ^ b
b = a ^ b
a = a ^ b
print(a ," ",b)


# Question 2 
# Check if a no. is of 3 digits
a = 321
print(a >= 100 and a <= 999)

# Question 3  
# Check if a year is leap year
# (rule 1-if year is completly divisbile by 4
# (rule 2-if year like in 100s eg- 1600 1900 2000 thenk check if century is divisble by 4)

y = 2000
print((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))


