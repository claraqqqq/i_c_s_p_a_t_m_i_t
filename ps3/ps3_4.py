# PRINTING OUT ALL AVAILABLE LETTERS  

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

"""
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getAvailableLetters(lettersGuessed)
abcdfghjlmnoqtuvwxyz
"""