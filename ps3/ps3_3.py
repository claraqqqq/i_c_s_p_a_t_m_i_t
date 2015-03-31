# PRINTING OUT THE USER'S GUESS

"""

GUESS USER THE PRINTING - 2 PART
parameters two in takes that getGuessedWord function the implement Next,
This lettersGuessed. letters, of list a and secretWord, string, a -
underscores, and letters of comprised is that string a returns function
shouldn't This secretWord. in are lettersGuessed in letters what on based
isWordGuessed! from different too be

Usage: Example

'apple' = secretWord >>>
's'] 'r', 'p', 'k', 'i', ['e', = lettersGuessed >>>
lettersGuessed) getGuessedWord(secretWord, print >>>
e' pp_ '_
at add to idea good a it's string, your into underscores inserting When
unguessed many how user the to clear it's so one, each after space a least
). _ _ _ _ with ____ of readability the (compare string the in left are letters
consider to programming, when important, very it's - usability called is This
to difficult program your find users If program. your of usability the
it! use won't they operate, or understand

our - wish you way any in spacing use to free are you problem, this For
proper the in are underscores and letters the that check only will grader
about think to you encourage do We spacing. at look not will it order;
desigining when usability

and secretWord in letters the all that assume may you function, this For
lowercase. are lettersGuessed

"""

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


"""
'apple' = secretWord >>>
's'] 'r', 'p', 'k', 'i', ['e', = lettersGuessed >>>
lettersGuessed) getGuessedWord(secretWord, print >>>
e' pp_ '_
"""

# rewrite 1
def getGuessedWord(secretWord, lettersGuessed):
    res = ''
    for idx in range(len(secretWord)):
        if secretWord[idx] in lettersGuessed:
            res += secretWord[idx]
        else:
            res += '_'
    return res
