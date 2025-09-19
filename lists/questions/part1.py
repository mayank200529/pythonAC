# # Create a list of five cities and print it.
# l = []
# n = int(input("Enter no of cities-"))
# for i in range(0,n):
#     l.append(input("Enter name of city-"))
# print(l)


l = [1,2,3,4,5,10]
print(l)

# Print the third element from a given list
print("Third element of list",l[2])

# Append the number 100 to a list of numbers.
l.append(100)
print(l)

# Insert the string "Python" at index 2 of a list.
l.insert(2,"Python")
print(l)

# Remove the first element from a list.
l.remove(l[0])
print(l)

# Reverse the elements of a list.
l.reverse()
print(l)

# Clone or copy a list using slicing or the copy() method.
l1 = l.copy()
print("using copy",l1)

l1 = l[:len(l)]
print("using slicing",l1)

# Check if a specific value exists in a list, and print a message.
val = str(input("Enter value-"))
i = 0
# while i<len(l):
if str(l[i]) == val:
    print(f"{val} is present in list")
else:
    print(f"{val} is not present in list")
i += 1
        

