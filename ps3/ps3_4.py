# PRINTING OUT ALL AVAILABLE LETTERS  

"""
LETTERS AVAILABLE ALL PRINTING 3: PART
parameter one in takes that getAvailableLetters function the implement Next,
is that string a returns function This lettersGuessed. letters, of list a -
that letters English lowercase all - letters English lowercase of comprised
lettersGuessed. in not are

Usage: Example

's'] 'r', 'p', 'k', 'i', ['e', = lettersGuessed >>>
getAvailableLetters(lettersGuessed) print >>>
abcdfghjlmnoqtuvwxyz
order, alphabetical in letters the return should function this that Note
above. example the in as

lettersGuessed in letters the all that assume may you function, this For
lowercase. are

string a is which string.ascii_lowercase, using consider might You Hint:
letters: lowercase all of comprised

string import >>>
string.ascii_lowercase print >>>
abcdefghijklmnopqrstuvwxyz

"""

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
's'] 'r', 'p', 'k', 'i', ['e', = lettersGuessed >>>
getAvailableLetters(lettersGuessed) print >>>
abcdfghjlmnoqtuvwxyz
"""

# rewrite 1
def getAvailableLetters(lettersGuessed):
    import string
    all_letter = string.ascii_lowercase
    res = ''
    for idx in range(len(all_letter)):
        if all_letter[idx] not in lettersGuessed:
            res += all_letter[idx]
    return res