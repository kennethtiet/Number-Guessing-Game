# Number-Guessing-Game

https://roadmap.sh/projects/number-guessing-game

1. Simply download the file

2. Run "python main.py"

3. Follow the instructions and play!

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have multiple chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances) Max Score: 0
2. Medium (5 chances) Max Score: 0
3. Hard (3 chances) Max Score: 0 

Enter a number: 1
Great! You have selected the Easy difficulty level.
Enter your guess: 50
Incorrect! The number is less than 50 .
Enter your guess: 25
Incorrect! The answer is greater than 25 .
Enter your guess: 37
Incorrect! The answer is greater than 37 .
Enter your guess: 43
You're close!
Incorrect! The number is less than 43 .
Enter your guess: 40
You're close!
Incorrect! The answer is greater than 40 .
Enter your guess: 41
You're close!
Incorrect! The answer is greater than 41 .
Enter your guess: 42
You're close!
Congratulations! You guessed the correct number in 7 attempts
It took you 39.325 seconds
Play again? y/n 
```

# Features:
- Users can play a guessing game
- Various difficulties offer different chances
- Users can play multiple rounds if prompted
- Timer added to see how long users take to win
- Hint system: If answer is within a value of 5 of the number
- User's high scores are stored per difficulty. Scores are calculated inversely (Max number of attempts - actual attempts).