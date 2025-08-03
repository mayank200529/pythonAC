#WAP to assign grade to student according to marks

a = input("Enter the name of student:")
b = int(input("Enter the marks out of 100:"))
if(b>=90 and b<=100):
    print("Congratulations, your grade is A")
elif(b>=80 and b<90):
    print("Congratulations, your grade is B")
elif(b>=70 and b<80):
    print("Congratulations, your grade is C")
elif(b>=60 and b<70):
    print("Your grade is D")
elif(b>=50 and b<60):
    print("Your grade is E+")
elif(b>=36 and b<50):
    print("Your grade is E")
elif(b<36 and b>=0):
    print("Your grade is F")
    print("You have to reattempt the exam")
elif(b<0):
    print("Marks cannot be -ve")
elif(b>100):
    print("You cannot obtain marks above 100")

# print("The grade shown above is of student-",a)

