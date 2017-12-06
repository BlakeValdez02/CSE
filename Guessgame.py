import random
randomNumber = random.randint(0,50)
print("Random number has been generated")
guessed = False
guesses_Taken = 0
while guessed==False and guesses_Taken > 5:
    userInput = int(input("Your guess please: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>100:
        print("Our guess range is between 0 and 50, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 50, please try a bit higher")
    elif userInput>randomNumber:
        guesses_Taken += 1
        print("Try again, a bit lower")
    elif userInput < randomNumber:
        print("Try again, a bit higher")

print("End of program")
