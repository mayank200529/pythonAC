# print("Q2 - WAP to print 1 + 2 + 3 + 4 + 5 = 15")
# print("Ans2 -")
n1 = 1
s1 = 0
while n1 <= 5:
    print(n1 , end = " + ")
    s1 = s1 + n1
    n1 = n1 + 1
print("\b\b=",s1)

# print("\n\nQ2b - WAP to print 2 + 4 + 6 + 8 + 10 = 30")
# print("Ans2b -")
n2 = 1
s2 = 0
while n2 <= 10:
    if n2 % 2 == 0:
        print(n2,end=" + ")
        s2 = s2 + n2
    n2 = n2 + 1
print("\b\b=",s2)

# print("\n\nQ2c - WAP to print 1 + 3 + 5 + 7 = 16")
# print("Ans2c -")
n3 = 1
s3 = 0
while n3 <= 7:
    if n3 % 2 != 0:
        print(n3,end=" + ")
        s3 = s3 + n3
    n3 = n3 + 1
print("\b\b=",s3)

# print("\n\nQ2d - WAP to print 10 + 9 + 8 + 7 + 6+ 5 + 4 + 3 + 2 + 1 = 55")
# print("Ans2d -")
n5 = 10
s5 = 0
while n5 <= 10 and n5 >= 1:
    print(n5,end = " + ")
    s5 = s5 + n5
    n5 = n5 - 1
print("\b\b=",s5)

# print("\n\nQ2e - WAP to print 10 + 8 + 6 + 4 + 2 = 30")
# print("Ans2e -")
n4 = 10
s4 = 0
while n4 <= 10 and n4>=0:
    if n4 % 2 == 0:
        print(n4,end = " + ")
        s4 = s4 + n4
    n4 = n4 - 1
print("\b\b=",s4)

#print("\n\nQ2f - WAP to print 720 , 120 , 24 , 6 , 2 , 1 ")
# print("Ans2f -")
n6 = 720
a = 6
while n6 <= 720 and n6 >= 1 and a>=1:
    print(n6 , end = " , ")
    n6 = n6 // a
    a = a - 1
print("\b\b ")

#print("\n\nQ2g - WAP to print 40230 + 5040 + 720 + 120 + 24 + 6 + 2 + 1 = 46233")
# print("Ans2g -")
n7 = 40320
a1 = 8
s7 = 0
while n7<=40320 and n7>=1 and a1>=1:
    print(n7 ,end=" + ")
    s7 = s7 + n7
    n7 = n7 // a1
    a1 = a1 - 1
print("\b\b=",s7)
