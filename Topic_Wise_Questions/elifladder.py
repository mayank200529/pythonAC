#Q1 WAP to take input of a student marks and display the grade
print("Q1 WAP to take input of a student marks and display the grade")
print("Ans1-")
mark = int(input("Enter the total marks of student Out of 100-"))
if mark >= 90 and mark <= 100:
    print("GRADE OF THE STUDENT IS - A")
elif mark >= 80 and mark <= 89:
    print("GRADE OF THE STUDENT IS - B")
elif mark >= 70 and mark <= 79:
    print("GRADE OF THE STUDENT IS - C")
elif mark >= 60 and mark <= 69:
    print("GRADE OF THE STUDENT IS - D")
elif mark >= 0 and mark <= 60:
    print("FAIL!!!")
else:
    print("Please enter marks in range 1 - 100")
  
#Q2 WAP to check if a number is +ve or -ve
print("Q2 WAP to check if a number is +ve or -ve or 0")
print("Ans2-")
num = int(input("Enter a number - "))
if num > 0:
    print("No. is positive")
elif num < 0:
    print("No. is negative")
else:
    print("No. is zero")

#Q3 WAP to ask the user to enter the day number (1–7) and print the corresponding weekday (1 = Monday … 7 = Sunday)
print("Q3 WAP to print weekday corresponding to no.")
print("Ans3-")
n1 = int(input("Enter a number to check weekday- "))
if n1 == 1:
    print("Monday")
elif n1 == 2:
    print("Tuesday")
elif n1 == 3:
    print("Wednesday")
elif n1 == 4:
    print("Thursday")
elif n1 == 5:
    print("Friday")
elif n1 == 6:
    print("Saturday")
elif n1 == 7:
    print("Sunday")
else:
    print("Invalid Input!!!")

#Q4 WAP to check if a given year is a leap year or not
print("WAP to check if a given year is a leap year or not")
print("Ans4-")
y = int(input("Enter year- "))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

#Q5 WAP that accepts a temperature in Celsius and classifies it as Cold (<10), Moderate (10–25), Warm (26–35), Hot (36–45), Very Hot (>45).
print("WAP that accepts a temperature in Celsius and classifies it")
print("Ans5 -")
T = int(input("Enter temprature -"))
if T < 10:
    print(f"Temprature is {T}°C which is classified as COLD")
elif T >= 10 and T <= 25:
    print(f"Temprature is {T}°C which is classified as MODERATE")
elif T >= 26 and T <= 35:
    print(f"Temprature is {T}°C which is classified as WARM")
elif T >= 36 and T <= 45:
    print(f"Temprature is {T}°C which is classified as HOT")
elif T > 45:
    print(f"Temprature is {T}°C which is classified as VERY HOT")