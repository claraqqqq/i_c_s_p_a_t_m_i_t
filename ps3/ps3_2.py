# HANGMAN PART 1: IS THE WORD GUESSED?

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
          
"""
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print isWordGuessed(secretWord, lettersGuessed)
False
"""