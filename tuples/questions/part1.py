
# QUESTION 1 
# FIND MAX MIN AND COUNT
t = (1,2,8,9,7,34,5,6,58,12)
print("max-",max(t))
print("min-",min(t))
print("count of 7 in tuple-",t.count(7))

#   QUESTION 2
# Make a tuple of student names and check if any name exist in the tuple or not
l = []
n = int(input("Enter no. of students-"))
for i in range(0,n):
    l.append(input("Enter name -"))
t = tuple(l)
print(t)
x = input("Enter name to search-")
# print(x in t)
c = False
for i in t:
    if i == x:
        print(f"{x} is present in tuple")
        c = True
        break
if c == False:
    print(f"{x} does not exist in tuple")

# QUESTION 3 
# create two tuple and concatenate them in one
t1 = (2,3,4,5,8,9)
t2 =  ("mayank","neha","lokesh")
print("concatenated tuple-",t1+t2)


# QUESTION 4
# find length of a tuple without len func
t1 = (2,3,4,5,8,9)
count = 0
for i in t1:
    count += 1
print("Length of tuple-",count)    

# QUESTION 5
# WAP to remove all duplicate values from tuple
t1 =(2,3,2,4,8,5,7,3,8,9)
t1 = tuple(set(t1))
print(t1)    


# QUESTION 6
# WAP to find a index for a given element in a tuple
t1 = (2,3,4,5,4,8,9)
# soln - with use of function
print("Index of 4 -",t1.index(4))

# soln - without using function
n = len(t1)
element = int(input("Enter element to find index-"))
print(f"Index of {element} is:")
for i in range(0,n):
    if t1[i] == element:
        print(i,sep ="," , end=" ")
# print("\b"," ")


# QUESTION 7
# WAP to create a nested tuple and access the inner nested elements
t = (1,(2,3),(5,(9,7)))
print(t)
print(t[1])
print(t[1][0])
print(t[2][1][0])

# QUETSTION 8
# WAP to check if a tuple is empty or not
t = ()
if len(t) == 0:
    print("Empty tuple")
else :
    print("Tuple is not empty")

# QUETSTION 8
# WAP to create a mix data tuple and sum the integer data
t1 = (2,3,"mahesh","nehal",4,5,8,9,"mayank","neha","lokesh")
sum = 0
for i in t1:
    if str(i).isnumeric() == True:
        sum = sum + i
print(sum)


