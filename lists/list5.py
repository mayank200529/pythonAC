# Functions of list
l = ["Mayank","Pal","Nishita"]

# 1-APPEND FUNCTION
print(l)
l.append("Lokesh")
print(l)

# 2 - INSERT FUNCTION
l.insert(2,"Mukul")
print(l)

# 3- EXTEND FUNCTION
l.extend(["Yash","Sahil","Rithik"])
print(l)

# 4 - REMOVE FUNCTION
l.remove("Lokesh")
print(l)

# 5 - POP FUNCTION
l.pop()
l.pop(3)
print(l)

# # 6- CLEAR FUNCTION
# l.clear()
# print(l)

# 6- INDEX and COUNT FUNCTION
x = l.index("Pal")
y = l.count("Pal")
print(l)
print("index of Pal is",x)
print("count of Pal is",y)

# 7- SORT FUNCTION
l.sort()
print(l)

l.sort(reverse=True)
print(l)

# 8 - SORTED FUNCTION
x = sorted(l)
# print("original list",l)
print("Sorted list",x)


# 9- REVERSE FUNCTION
l.reverse()
print(l)

# 10- COPY function
y = l.copy()
print(l)
print(y)

# 11- Length function
x = len(l)
print(x)


# 11- MAX & MIN FUNCTION
l1= [1,5,8,9,3,44,7,5]
x = max(l1)
y = min(l1)
print("max is: ",x,"Min is: ",y)

# SUM FUNCTION
s = sum(l1)
print("Sum is: ",s)