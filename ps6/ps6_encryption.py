# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:/Users/xiali/python/words_ps6.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

# print string.ascii_lowercase

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.    
    #return "Not yet implemented." # Remove this comment when you code the function
    lowcase = string.ascii_lowercase + string.ascii_lowercase
    upcase = string.ascii_uppercase + string.ascii_uppercase
    lowDict = {}
    upDict = {}
    for index in range(26):
        lowDict[lowcase[index]] = lowcase[index + shift]
        upDict[upcase[index]] = upcase[index + shift]
    return dict(lowDict.items() + upDict.items())
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    encodeText = ''
    for letter in text:
        if (letter not in string.punctuation) \
             and (letter not in string.digits) \
             and (letter != ' '):
            encodeText += coder[letter]
        else:
            encodeText += letter
    return encodeText


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    #return "Not yet implemented." # Remove this comment when you code the function
    return applyCoder(text, buildCoder(shift))


#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    #return "Not yet implemented." # Remove this comment when you code the function
    """
    shift = 0
    for shiftTmp in range(26):
        label = True
        wordListShift = applyShift(text, shiftTmp)       
        newList = wordListShift.split(' ')
        print newList
        for word in newList:
            if not isWord(wordList, word):
                label = False
        if label == True:
            shift = shiftTmp
    return shift
    """
    shift = 0
    countInit = 0
    for shiftTmp in range(26):
        count = 0
        wordListShift = applyShift(text, shiftTmp)       
        newList = wordListShift.split(' ')
        for word in newList:
            if isWord(wordList, word):
                count += 1
        if countInit < count:
            shift = shiftTmp
            countInit = count
    return shift


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    shift = findBestShift(loadWords(), getStoryString())
    return applyShift(getStoryString(), shift)


#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
