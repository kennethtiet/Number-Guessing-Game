import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 changes to guess the correct number.\n")

while(True):
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

    inp = input("Enter a number: ")
    difficulty = "N/A"
    chances = -1

    if inp == "1":
        difficulty = "Easy"
        chances = 10
        break
    elif inp == "2":
        difficulty = "Medium"
        chances = 5
        break
    elif inp == "3":
        difficulty = "Hard"
        chances = 3
        break
    else:
        print("Select a valid number.\n")

    
print("Great! You have selected the", difficulty,"difficulty level.")

#generate number
num = random.randrange(0, 100, 1)
attempts = 0
while attempts < chances:
    answer = int(input("Enter your guess: "))
    attempts += 1
    if answer == num:
        print("Congratulations! You guessed the correct number in", attempts,"attempts")
        break
    elif answer > num:
        print("Incorrect! The number is less than", answer,".")
    else:
        print("Incorrect! The answer is greater than ",answer,".")
        
if attempts >= chances:
    print("Ran out of attempts! The number was ", num)