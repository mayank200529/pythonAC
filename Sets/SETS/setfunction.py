"""
# Methods on sets

add() #ADD ELEMNT TO SET
clear() 
copy()
discard()
pop()
remove()
update()

"""

a = {"ajay","mayank","pal","neha"}
a.add("nishita")
print("ADDED -",a)
a.remove("ajay")
print(a)
a.pop()
print(a)
a.discard("neha")
print(a)
a.clear
print(a)
b = a.copy()
print(b)



# Special methords 
# 1. UNION
a = {"ajay","mayank","pal","neha"}
b = {"mukul","lokesh","ajay","nishita"}
print(a)
print(b)
print("\nUNION")
print(a | b)      #UNION can be written as this 
print(a.union(b)) #UNION can be written as this also

# 2. Intersection
print("\nIntersection")
print(a & b)      #intersection can be written as this 
print(a.intersection(b)) #intersection can be written as this also

# 3. Difference
print("\nDifference")
print(a - b)      #difference can be written as this 
print(a.difference(b)) #difference can be written as this also

# 4. Symmertic Difference
print("\nSymmertic Difference")
print(a - b)      #Symmertic difference can be written as this 
print(a.symmetric_difference(b)) #Symmertic difference can be written as this also
