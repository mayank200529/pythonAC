# SETS in {}
# Store only unique data
# When we print sets then it generate output in random order
# No data is repeated in output

# you cannot apply range and index on sets (NOT SCRIPTABLE)
# you cannot add and multiply two sets( set1 + set2: ERROR, set1 * set2: ERROR)
a = {"ajay","mayank","pal","neha"}
print(type(a))
print(a)
# Access elements of sets
for i in a:
    print(i,end=" ")

print()
# check if element present in set
print("mayank" in a)

"""
a = {1,2,32,45,15,6,77,8,19,10,11,12}
print(a)
"""