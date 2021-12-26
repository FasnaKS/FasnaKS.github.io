import random
import time

name = input("Enter your name")
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)
hang = ["""
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

play_game = ""


def getRandomWord():
    Category = int(input(" please select a category..\n 1. ANIMALS\n 2.FRUITS \n "
                         "3.VEGETABLES \n 4.FLOWERS  \n Enter a number between 1 and 4!!\n"))
    if Category == 1:
        words = ['dog', 'cow', 'buffalo', 'lion', 'tiger', 'giraffe', 'deer', 'cat', 'kangaroo', 'pig',
                 'bear', 'elephant', 'goat', 'fox', 'bull', 'camel', 'cheetah', 'chimpanzee', 'donkey', 'hippopotamus',
                 'hyena', 'squirrel', 'jaguar', 'leopard', 'lizard', 'rat']
        word = random.choice(words)
        return word
    elif Category == 2:
        words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
                 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee',
                 'muskmelon']
        word = random.choice(words)
        return word

    elif Category == 3:
        words = ['tomato', 'potato', 'pumpkin', 'bitter gourd', 'zucchini', 'cabbage', 'eggplant',
                 'cauliflower', 'peas', 'beans', 'beetroot', 'carrot', 'cucumber', 'lettuce',
                 'snake gourd', 'capsicum']
        word = random.choice(words)
        return word
    elif Category == 4:
        words = ['hibiscus', 'rose', 'jasmine', 'tulip', 'sunflower', 'lily', 'dahlia', 'lotus',
                 'marigold', 'daffodil', 'orchid',
                 'daisy', 'lavender', 'chrysanthemum', 'bougainvillea', 'pansy']
        word = random.choice(words)
        return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        return play_game.lower().startswith('y')
    elif play_game == "n":
        print("Thank you for playing!!")


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break
