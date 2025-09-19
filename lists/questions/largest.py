# find largest and smallest no. of list
# Find the index of the maximum and minimum value in a list.
nums = []
a = int(input("Enter no. of element in list:"))
for i in range(0,a):
    nums.append(int(input("Enter elements-")))
largest = float("-inf")
smallest = float("inf")
for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        a = i
    if nums[i]<smallest:
        smallest = nums[i]
        b = i
print("Largest-",largest,"Index-",a,"Smallest-",smallest,"Index-",b)