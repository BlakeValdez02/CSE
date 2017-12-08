import random
import sys
randomNumber = random.randint(0, 50)
print("Random number has been generated. You have 5 tries.")
guessed = False
guesses_Taken = 5
while guessed==False:

    userInput = int(input("Your guess please: "))
    guesses_Taken -= 1
    if guesses_Taken > 0:
        if userInput == randomNumber:
            guessed = True
            print("Well done!")
        elif userInput > 50:
            print("Our guess range is between 0 and 50, please try a bit lower")
        elif userInput < 0:
            print("Our guess range is between 0 and 50, please try a bit higher")
        elif userInput > randomNumber:
            print("Try again, a bit lower")
        elif userInput < randomNumber:
            print("Try again, a bit higher")
    else:
        print("You have run out of tries. Game Over")
        sys.exit(0)

print("End of program")
