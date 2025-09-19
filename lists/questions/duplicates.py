# To remove duplicate element from an array

nums = list(map(int,input("Enter elements of list-").split()))

n = len(nums)
my_dict = {}
for i in range(0,n):
    my_dict[nums[i]] = 0
j = 0
for k in my_dict:
    nums[j] = k
    j += 1
print("Unique elements-",j)