'''
Write a random number guesser game. in this game, the computer will 
think of a number between 1 to 100 and the player will guess the number. 
The player has 7 chances to guess the number.
After each try, the computer will the player one of the following:
1. The player's guess is too big
2. The player's guess is too small
3. The player's guess is correct! (Game ends)

If the player did not guess correctly after 7 times, 
the program will tell the player the answer.
'''

import random
randomnumber = random.randint(1,100)
#print("the random number is", randomnumber)
winGame = False

for count in range(7):
    answer = input("Guess a numberbetween 1 and 100:")
    answer = int(answer)
    if answer == randomnumber:
        print("You got it, the answer is", randomnumber)
        winGame = True
        break
    if answer > randomnumber:
        print("try a smaller number")
    else:
        print("try a bigger number")

if winGame:
    print()

else:
    print("Game over, you used up all your tries:(")