# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
WORDLIST_FILENAME = "C:/Users/xiali/python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
       if char in lettersGuessed:
          lettersGuessed.remove(char)
       else:
          return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lenghtsecretWord = len(secretWord)
    stuffedWord = '_'
    guessedWord = ''
    # for ii in range(lenghtsecretWord):
    #   guessedWord += '_'
    # letterGuessedColon = lettersGuessed
    for ii in range(lenghtsecretWord):
       if secretWord[ii] in lettersGuessed:
          guessedWord += secretWord[ii]
          # letterGuessedColon.remove(char)
       else:
          guessedWord += stuffedWord
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersGuessed.sort()
    import string
    allLetters = string.ascii_lowercase
    lettersAvailable = ''
    for ii in range(len(allLetters)):
       if allLetters[ii] not in lettersGuessed:
          lettersAvailable += allLetters[ii]
    return lettersAvailable
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    
    print "Welcome to the game, Hangman!"
    lengthSecretWord = len(secretWord)
    print "I am thinking of a word that is " + str(lengthSecretWord) + " letters long."
    
    cnt = 8
    label = True
    
    lettersGuessed = []
    
    while cnt > 0 and label:
        print "-------------"
        print "You have " + str(cnt) + " guesses left."
        
        lettersAvailable = getAvailableLetters(lettersGuessed)
        print "Available letters: " + str(lettersAvailable)
        
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
                
        if guess in secretWord:
            if guess in lettersGuessed:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)               
                if isWordGuessed(secretWord, lettersGuessed):
                    label = False
                    print "-------------"
                    print "Congratulations, you won!"
        else:
            if guess in lettersGuessed:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                cnt -= 1
                if cnt == 0:
                    print "-------------"
                    print "Sorry, you ran out of guesses. The word was " + secretWord
                





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
