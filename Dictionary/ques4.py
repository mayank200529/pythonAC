# WAP to sort dictionary by its keys and print result
sort = {91:"Mayank",110:"Pal",104:"Neha",82:"Lokesh"}
sort = dict(sorted(sort.items()))
print(sort)


# WAP to get sum of all values in dict
dict_sum = {2:4,5:10,7:49,9:81}
sum = 0
for i in dict_sum:
    sum = sum + dict_sum[i]
print("SUM of dict values-",sum)

# WAP to reverse the keys and values
d = {1:"A",2:"B"} 
print("Original-",d)
nd = {}
for key,val in d.items():
    nd[val] = key
print("Reversed-",nd)

# or

nd = {val:key for key,val in d.items()}  #Single line reverse

# Write a program to update a dictionary by adding a new key only if it doesn’t exist.
d = {"India":"Delhi","Japan":"Tokyo","USA":"Washington DC","Russia":"Moscow","France":"Paris"}
print(d)
key = input("Enter key-")
if key not in d.keys():
    val = input("Enter value-")
    d[key] = val
    print(d)
else:
    print("Key already exists")

