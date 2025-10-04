# Tuples are similar to list
# but it is immutable (we cannot perform any change in index)
# All data in tuple store inin indexes
t = ()
print(type(t))

# Declaration of tuple

t = (1,2,"a","b")
t = ()
t = tuple()

# conversion of list to tuple
l = [1,3,5,7]
t = tuple(l)
print(t," ",type(t))

# Access the elemnts of tuple
t = (1,5,7,9,17,19)

print(t[2])

for i in t :
    print(i,end=" ")
print()

for i in range(len(t)):
    print(t[i],end=" ")
print()


# Slicing in tuple 
t = (1,5,7,9,17,19)
print(t[:])
print(t[3:])
print(t[:4])
print(t[1:6:2])
print(t[-1::-1])