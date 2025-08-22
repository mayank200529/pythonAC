# DAY 5 :(

#LOOPS IN PYTHON
#two types - while and for

# count = 1  #count is a variable and it is called iterator
# while count<=5 :
#     print("mayank")
#     count += 1
# print(count)
# #                        OR
# i = 1
# while i<=5:
#     print("hello")
#     i +=1
# print(count)

# #PRINT NUMBERS FROM 1 TO 5
# i = 1
# while i<=5:
#     print(i)
#     i += 1
# print("Loop Ended")

# #PRINT NUMBERS FROM 1 TO 5 in reverse
# i = 5
# while i>=1:
#     print(i)
#     i -= 1
# print("Loop ended")


# #WAP TO PRINT NO.S FROM 1 TO 100
# i = 1
# while i<=100:
#     print(i)
#     i +=1
# print("ALL THE NO.S FROM 1 TO 100 ARE PRINTED SUCCESFULLY :) ")

# #WAP TO PRINT NO.S FROM 100 TO 1
# i = 100
# while i>=1:
#     print(i)
#     i-=1
# print("ALL THE NO.S FROM 100 TO 1 ARE PRINTED SUCCESFULLY :) ")


# #WAP TO PRINT MULTIPLICATION TABLE OF NUMBER 'n'

# n= int(input("enter number :"))
# i=1
# while i<=10:
#     print(n*i)
#     i +=1


# #WAP TO PRINT ELEMENT OF FOLLOWING LIST USING LOOP
# # [1,9,16,25,36,49,64,81,100]
# nums = [1,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

# #WAP TO SEARCH FOR NUMBER x IN A TUPLE USING LOOP
# # (1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found at idx",i)
#         break
#     else:
#         print("finding")
#     i+=1

# #CONTINUE STATEMENT WORKING
# i = 0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i += 1


# #WAP TO PRINT ALL EVEN NO.S FROM 1 TO 10 USING LOOP
# i=1
# while i<=10:
#     (i%2==0)
#     print(i,"is even")
#     i+=1   


#FOR LOOPS
#THESE ARE USED FOR SEQUENTIAL TRAVERSAL.
#FOR TRAVERSING LIST STRING TUPLE ETC.

#SYNTAX
# for el in list:
    # print(el)


#example
nums = [1,2,3,4,5]

for val in nums:
    print(val)

#example 
tuple = (1,2,3,4,5)

for nums in tuple:
    print(nums)

#example
str = "mayankrawat"
for character in str:
    if (character == 'r'):
        print("r found")
        break
    print(character)
else:
    print("END")


