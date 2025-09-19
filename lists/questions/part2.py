# Merge two list
arr1 = [1,2,3,4,5]
arr2 = [3,5,8,9,11]
arr3 = arr1 + arr2
print("Merge list-",arr3)

print()
# Given two lists, print only the common elements.
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            print(f"{arr1[i]} is common")

print("Common elements-")
for i in arr1:
    if i in arr2:
        print(i,end=" ")


print()
l = [100, 10, 5, 4, 3, 'Python', 2]
# Iterate over a list and print every element with its index
for i in range(len(l)):
    print(f"Element {i+1}:",l[i]," Index:",i,end="\n")


print()
# Count the number of occurrences of the value 5 in a list.
l = [1,3,5,5,3,6,8,4,5,6,5,6,5,5,4,6,5,25,1]
count=0
for i in range(len(l)):
    if l[i] == 5:
        count += 1
print("Occurance of five:",count)


print()
# Access and print the value 400 from this list: [10, [20, 30], [300, 400, 500]].
list =  [10, [20, 30], [300, 400, 500]]
print(list[2][1])