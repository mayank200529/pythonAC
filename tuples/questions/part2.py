# QUESTION 1
# WAP TO SORT ELEMENTS OF TUPLE IN ASCENDING AND DESCENDING ORDER
t = (5,7,2,6,4,1,9)
t = sorted(t)
print("Ascending-",t)
print("Descending-",t[-1::-1])

# QUESTION 2
# WAP to slice a tuple into two parts and display them
t = (5,7,2,6,4,1,9)
print(t)
print("Part 1-",t[:3])
print("Part 2-",t[3:])

# QUESTION 3
# WAP TO find all even and odd no.s from tuple
t = (5,7,2,6,4,1,9)
for i in range(0,len(t)):
    if t[i] % 2 == 0:
        print("EVEN:",t[i],end=", ")
    elif t[i] % 2 != 0:
        print("ODD:",t[i],end=", ")
print("\b\b"," ")

# QUESTION 4
# WAP to unpack a tuple of 5 value into 5 separate variable
t = (1,2,3,4,5)
l = ["a","b","c","d","e"]
i = 0
pass

#  QUESTION 5
# WAP to create a tuple of string and join them
t = ("My","Name","Is","Mayank")
l = list(t)

s1 = "My name is Mayank"
s2 = "Her name is Pal"
x = s1.split(" ") + s2.split(" ")
l = tuple(x)
print(l)