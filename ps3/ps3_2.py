# HANGMAN PART 1: IS THE WORD GUESSED?

"""

GUESSED WORD THE IS 1: PART
problem. this starting before Introduction Hangman the read Please
exercises three next the in creating be will you functions helper The
want you if them implement to have DO you but suggestions, simply are
structure to prefer you'd If Set. Problem Hangman this for points get to
Problem this redo to free feel way, different a in program Hangman your
a at or programming, to new you're if However, way. different a in Set
you that suggest strongly we program, this construct to how of loss
Hangman to on continuing before functions helper three next the implement
2. Part

code easily us help will that functions simple 3 writing by start We'll
that isWordGuessed function the implement First, problem. Hangman the
letters, of list a and secretWord, string, a - parameters two in takes
secretWord if True - boolean a returns function This lettersGuessed.
lettersGuessed) in are secretWord of letters the all (ie, guessed been has
otherwise. False and

Usage: Example

'apple' = secretWord >>>
's'] 'r', 'p', 'k', 'i', ['e', = lettersGuessed >>>
lettersGuessed) isWordGuessed(secretWord, print >>>
False
and secretWord in letters the all that assume may you function, this For
lowercase. are lettersGuessed

"""

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
          
# rewrite 1

def isWordGuessed(secretWord, lettersGuessed):
    lettersGuessed_copy = lettersGuessed
    for idx in range(len(secretWord)):
        if secretWord[idx] in lettersGuessed_copy:
            lettersGuessed_copy.remove(secretWord[idx])
        else:
            return False
    return True 
