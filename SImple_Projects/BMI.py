#WAP to classify a person's BMI into different categories
print("Hello!\nThis program will help you to know your health stauts according to BMI")
print("Please enter 1 if you know your bmi or enter 2 to calculate BMI")
n = int(input("Enter here - "))
if n == 1:
    bmi = int(input("Enter the body mass index(BMI) -"))
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Healthy Weight")
    elif bmi >= 25.0 and bmi <= 29.9:
        print("Overweight")
    elif bmi >= 30:
        print("Obese")
    else:
        print("Invalid Input of BMI")
if n == 2:
    weight = int(input("Enter weight in Kg- "))
    height = int(input("Enter height in meters- "))
    calc_bmi = (weight) % (height * height)
    print(f"Your BMI is {calc_bmi}")
