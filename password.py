# Download the file and put in into any IDE to use!

import random

# password variables
alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
numbers = '1234567890'
symbols = '!@#$%^&*_'

# random junk (must be len(x) - 1 or the program has a chance to commit suicide)
randomAlphabet = random.randint(0, len(alphabet) - 1)
randomNumber = random.randint(0, len(numbers) - 1)
randomSymbol = random.randint(0, len(symbols) - 1)

# password properties
characterPossibilities = [alphabet[randomAlphabet], numbers[randomNumber], symbols[randomSymbol]] 
characterCount = input('Amount of characters: ')
chosenPassword = ''
chosenCharacter = characterPossibilities[random.randint(0, len(characterPossibilities) - 1)]

# the most horrible loop ever (dont look at it for your own sake)
for i in range(int(characterCount)):
    # resets the characters
    randomAlphabet = random.randint(0, len(alphabet) - 1)
    randomNumber = random.randint(0, len(numbers) - 1)
    randomSymbol = random.randint(0, len(symbols) - 1)
    # resets the possibilities
    characterPossibilities = [alphabet[randomAlphabet], numbers[randomNumber], symbols[randomSymbol]]
    chosenCharacter = characterPossibilities[random.randint(0, len(characterPossibilities) - 1)]
    # adds a character to the password
    chosenPassword += chosenCharacter

print('Recommended Password: ' + chosenPassword)