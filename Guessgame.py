import random
randomNumber = random.randrange(0,100)
print("Random number created")
guessed = False
while guessed==False:
    userInput = int(input("What is your guess?: "))
    if userInput==randomNumber:
        guessed = True
        print("Good Job!")
    elif userInput>50:
        print("Our guess range is between 0 and 50, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 50, please try a bit higher")
    elif userInput>randomNumber:
        print("Try again, a bit lower")
    elif userInput < randomNumber:
        print("Try again, a bit higher")
    elif userInput > randomNumber:
        print("Try again, a bit lower")
    elif userInput < randomNumber:
        print("Try again, a bit higher")
    elif userInput>randomNumber:
        print("Try again, a bit lower")
    elif userInput < randomNumber:
        print("Try again, a bit higher")
    elif userInput > randomNumber:
        print("Try again, a bit lower")
    elif userInput < randomNumber:
        print("Try again, a bit higher")
    elif userInput>randomNumber:
        print("Try again, a bit lower")
    elif userInput < randomNumber:
        print("Try again, a bit higher")
        print("End of the game")