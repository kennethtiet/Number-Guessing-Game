import random
import time

max_score = [10,5,3]
level = -1
while(True):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have multiple chances to guess the correct number.\n")

    while(True):
        print("Please select the difficulty level:")
        print("1. Easy (10 chances) Max Score:", 10 - max_score[0])
        print("2. Medium (5 chances) Max Score:", 5 - max_score[1])
        print("3. Hard (3 chances) Max Score:", 3 - max_score[2], "\n")

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

    level = int(inp)
    print("Great! You have selected the", difficulty,"difficulty level.")

    start = time.time()
    #generate number
    num = random.randrange(0, 100, 1)
    attempts = 0
    while attempts < chances:
        answer = int(input("Enter your guess: "))
        attempts += 1
        if abs(answer - num) < 5:
            print("You're close!")
        
        if answer == num:
            end = time.time()
            length = end - start
            
            if attempts < max_score[level-1]:
                max_score[level-1] = attempts
            
            print("Congratulations! You guessed the correct number in", attempts,"attempts")
            print(f"It took you {length:.3f} seconds")
            break
        elif answer > num:
            print("Incorrect! The number is less than " + str(answer) + ".")
        else:
            print("Incorrect! The answer is greater than " + str(answer) + ".")
            
            
    if attempts >= chances:
        print("Ran out of attempts! The number was", num)

    inp = input("Play again? y/n ")

    if inp == "n":
        break