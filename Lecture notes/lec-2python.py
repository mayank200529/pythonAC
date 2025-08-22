#DAY2 :)
# #STRING CONCEPTS AND BASICS

# str1 = "sting can be written in double inverted comma"
# str2 = 'string can be can be written in single inverted comma'
# str3 = '''string can be can be written in triple inverted comma'''

# print(str1)
# print(str2)
# print(str3)

# str4 = "My name is Mayank singh rawat.\nIt's my second day of learning python."
# print(str4)

# #concatenation 
# #(adding two strings)
# str5 = "Hello"
# str6 = "World"
# final_str = str5 + str6
# final_str1 = str5 + " " + str6 
# print(final_str)
# print(final_str1)

# #length of str
# print(len(str5))
# #(or)
# len2 = len(str6)
# print(len2)
# print(len(final_str))
# print(len(final_str1))

# #Indexing
# str7 = "apna college"
# print(str7[0])
# ch = str7[2]
# print(ch)

# #SLICNING
# #(Accessing parts of string)
# str8 = "ApnaCollege"
# print(str8[1:5])
# print(str8[0:3])
# print(str8[4:11])
# print(str8[4:len(str8)])#to go to last we can also write len of string
# print(str8[4:])#auto till end
# print(str8[:5])#auto start from 0
#   #negative indexing
# print(str8[-5:-1])


# #FUNCTIONS IN STRING
# str9 = "i am a coder"
# #1 .endswith
# print(str9.endswith("der"))
# print(str9.endswith("cod"))
# #(endswith functions returns true if correct words are at the end)

# # 2 .capitalize
# str9 = str9.capitalize()
# # print(str9.capitalize())
# print(str9)
# #(capitalize function makes the first character capital)

# #3 .replace
# str = "I am studying python from apna college"
# print(str.replace("python","C++"))
# str1 = "I am studying pyhton from apna college"
# print(str1.replace("o","a"))
# #(replace function can replace a char of word from string)

# #4 .find
# str = "I am studying pyhton from apna college"
# print(str.find("o"))
# print(str.find("am"))
# print(str.find("q"))
# #returns index of char or word
# #when we find word or char which do not exist then it returns -1

# #5 .count
# str = "I am studying from pyhton from apna college"
# print(str.count("o"))
# print(str.count("from"))
# #(it gives no of repetation of a char or word in a string)


# #WAP to input user first name and print its length
# name = input("Enter your first name:")
# print("Length of your name is:",len(name))


# #WAP to find occurance of '$' in a string
# str = "This is a $ symbol use $string"
# print("Total no. of times the symbol $ is used is:",str.count("$"))

## conditional statements
# age = int(input("Enter your age:"))
# if(age>=18):
#     print("Hurahh!! You are eligible to drive as you have a license :)")
# elif(age==17):
#     print("You have wait for one more year to drive :(")
# else:
#     print("Sorry you cannot drive as you dont have a license :(")

# light = input("Enter the color of light in capital letters:")

# if(light == "RED"):
#     print("stop")
# elif(light == "GREEN"):
#     print("go")
# elif(light == "YELLOW"):
#     print("wait")
# else:
#     print("The colour you entered is not used in traffic lights")

# #WAP to check if an number is =ve,-ve or 0
# a = float(input("Enter the number:"))
# if(a>0):
#     print("The given number is +ve")
# elif(a<0):
#     print("The given number is -ve")
# else:
#     print("The given number is 0")

# #WAP to assign grade to student according to marks

# a = input("Enter the name of student:")
# b = int(input("Enter the marks out of 100:"))
# if(b>=90 and b<=100):
#     print("Congratulations, your grade is A")
# elif(b>=80 and b<90):
#     print("Congratulations, your grade is B")
# elif(b>=70 and b<80):
#     print("Congratulations, your grade is C")
# elif(b>=60 and b<70):
#     print("Your grade is D")
# elif(b>=50 and b<60):
#     print("Your grade is E+")
# elif(b>=36 and b<50):
#     print("Your grade is E")
# elif(b<36 and b>=0):
#     print("Your grade is F")
#     print("You have to reattempt the exam")
# elif(b<0):
#     print("Marks cannot be -ve")
# elif(b>100):
#     print("You cannot obtain marks above 100")

# # print("The grade shown above is of student-",a)


# # nested statements
# age = int(input("Enter age->:"))
# if(age>=18):  #NESTING
#     if(age>=80):
#         print("cannot vote")
#     else:
#         print("can vote")
# #nesting means if statement inside if statement

# #WAP to find greatest of 3no.s
# a = float(input("Enter first number:"))
# b = float(input("Enter second number:"))
# c = float(input("Enter third number:"))
# if(a>=b and a>=c):
#     print("The greatest no. is:",a)
# elif(b>=c):
#     print("The greatest no. is:",b)
# else:
#     print("The greatest no. is:",c)

# #WAP to check if no. is multiple of 7 or not
# a = int(input("enter your number:-"))
# if(a%7==0):
#     print("The given number is divisible by 7")
# else:
#     print("The given number is not divisible by 7")
