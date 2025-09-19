nums = []
for i in range(5):
    nums.append(int(input(f"Enter {i+1} number-")))
print("list=",nums)

# sum
sum = 0
n = len(nums)
for i in range(0,n):
    sum = sum + nums[i]
print("Sum =",sum)

# multiply
mult = 1
n = len(nums)
for i in range(0,n):
    mult = mult * nums[i]
print("multiplication =",mult)