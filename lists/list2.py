l1 = ["ajay","Mayank","pal","Neha"]
l2 = ["a","b","c","d","e"]
# listt can be repeated multiple times
print(l1 * 2)

# list can be concatenated
print(l2 + l1)


# join string
s = " -> ".join(l1)
print(s)

# split string in list
string = "My name is mayank singh rawat"
l = string.split(" ")
print(l)

# user input of list
l = []
for i in range(5):
    l.append(input("Enter a data - "))
print(l)

# reverse of a string
l = []
for i in range(5):
    l.append(input("Enter a data - "))
print(l[-1::-1])

