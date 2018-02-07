import random
import string
text = list

# This is a guide of how to
# make hangman
# 1. Make a word bank - 10 items
# 2. Select a random item to guess
# 4. Reveal Letters based on input# 3. Hide the word (use *)
# 5. Create win and lose conditions
# userInput = int(input("Guess a letter: "))

alphabet = string.ascii_lowercase
word_bank = ['Cheddar', 'Swiss', 'American', 'Monterrey Jack', 'Mozzarella', 'Provolone', 'Pepper Jack', 'Gouda',
             'Blue Cheese', 'Ricotta', 'Feta']

guesses_left = 10
regular_word = text(random.choice(word_bank).lower())
word = ''.join(regular_word)
guesses = [' ']
hidden_word = ('*' * len(regular_word))
print(hidden_word)
while guesses_left > 0:
    print(guesses)
    print("The word is %s letters long" % len(regular_word))
    player_guess = input("Take a guess:").lower()
    guesses.append(player_guess)
    if player_guess not in regular_word:
        guesses_left -= 1
    print("You now have %s guesses" % guesses_left)
    output = []
    for letter in regular_word:
        if letter in guesses:
            output.append(letter)
        else:
            output.append('*')
    output = ''.join(output)
    if '*' not in output:
        print("You win. The word was %s" % word)
        exit(0)
    print(output)
print("You lose. The word was %s" % word)