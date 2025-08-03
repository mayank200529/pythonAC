print("Welcome")
print("This is a quiz which is based on your knowledge about one of the major Sanskrit epic of India 'THE MAHABHARATA'\n")
answer = input("Are you ready for this quiz?")

if answer.lower() != "yes":
    quit()
    
print("\nThere will be three questions in the quiz")
print("For every correct answer you will get 5  points")
print("For every incorrect answer you will get 0  points\n")
print("Give your answer by selecting a/b/c.")
points = 0

print("Question 1:- The Mahabharata mentions the birth of Lord Vishnu in a human form named\na:Rama\nb:Krishna\nc:Narsimha\n")
answer = input("ANSWER:- ")
if answer.lower() == "b":
    print("Correct!\n")
    points += 5
else:
    print("Incorrect\n")
    
print("Question 2:- Karna, who was a son of Kunti, was cursed by the rishi parshuram because\na:he hid his identity\nb:he revealed the future\nc:he was born with armour and earrings attached to him\n")
answer = input("ANSWER:-")
if answer.lower() == "a":
    print("Correct!\n")
    points += 5
else:
    print("Incorrect\n")
    
print("Question 3:- In the great war of Mahabharatha, the age of Bhishma Pitamah was\na:124 years\nb:132 years\nc:130 years\n")
answer = input("ANSWER:- ")
if answer.lower() == "c":
    print("Correct!\n")
    points += 5
else:
    print("Incorrect\n")
 
print("HURRAH! YOU HAVE SUCCESSFULLY COMPLETED THE QUIZ :)")   
print("You got " + str(points) + " points out of 15")


print("⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⢸⡟⠛⢳⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⢸⡋⢺⡏⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠘⣷⡀⢹⡀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠹⣧⠀⠻⡄⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠹⣧⠀⢱⡄⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠙⣧⠀⢱⡀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠙⣧⠀⢳⡀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠸⣧⠀⢧⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⢹⣆⠘⢧⠈⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢻⡄⠘⣆⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠘⡄⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠹⡄⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⢹⡀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⢳⡀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣯⠀⢣⡀⠻⣶⣶⣦⣤⣤⣴⣾⡻⣧⡄")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠈⢷⠀⠙⢛⡆⢸⡶⠾⠋⣳⠙⣧")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢻⣇⣼⣿⡛⠋⣀⡾⢴⣾⣿⠿⠟⠋")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣦⣀⣁⣀⣹⢷⡎⢻⡷⠛⠉⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣴⣞⠿⠚⣉⣁⣽⣿⣿⡴⠖⠋⢻⣆⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⣴⣪⣿⠟⠋⠉⠉⢻⣦⠴⠎⢻⡄⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠋⠁⠀⠀⠀⠀⠀⠀⢹⣶⠒⠙⣷⣀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣻⡟⣿⠄⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⡟⠀⠀⠀")