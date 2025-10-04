# # Operations on tuple
# t = (1,3,4,5,7,8,9,23,34,14,56)
# print(t*3)
# print(t+t)

# Functions of tuples
t = tuple([1,3,4,5,3,7,8,9,23,34,14,56])
print(t)
print("length of tuple-", len(t))
print("max-",max(t))
print("min-",min(t))
print("sum-",sum(t))
print("Sorted-",sorted(t))
print("count of 3 in tuple-",t.count(3))
print("Index of 3:",t.index(3))


# user input tuple
l = []
n = int(input("Enter no. of elements-"))
for i in range(0,n):
    l.append(input("Enter element -"))
t = tuple(l)
print(t,"  ",type(t))


# imutablity of tuples
t = (1,3,4,5,7,8,9,23,34,14,56)
t[1] = 14