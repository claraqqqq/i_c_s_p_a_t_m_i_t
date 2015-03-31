#HANGMAN THE GAME  

"""

- parameter one takes which hangman, function the implement will you Now
game interactive an up starts This guess. to is user the secretWord the
advantage take you sure Be computer. the and user the between Hangman of
and getGuessedWord, isWordGuessed, functions, helper three the of
part. previous the in defined you've that getAvailableLetters,

Hints:
functions provided the using we're where noticing by start should You
one. random a pick and words the load to ps3_hangman.py) of top the (at
on used be only should chooseWord and loadWords functions the that Note
in solution your in enter you When tutor. the in not machine, local your
function. hangman your give to need only you tutor, the

example: For case. lower to input user convert to lower() using Consider

'A' = guess
guess.lower() = guessInLowerCase
them! need you if functions helper additional writing Consider

store: to wish may you information of pieces important four are There

guess. to word The secretWord:
far. so guessed been have that letters The lettersGuessed:
far. so made guesses incorrect of number The mistakesMade:
a time Every guessed. be still may that letters The availableLetters:
from removed be must letter guessed the letter, a guesses player
availableLetters, in not is that letter a guess they if (and availableLetters
- that guessed already they've them telling message a print should you
again!). try so

Output Sample
this... like look should game winning a of output The
file... from list word Loading
loaded. words 55900
Hangman! game, the to Welcome
long. letters 4 is that word a of thinking am I
-------------
left. guesses 8 have You
abcdefghijklmnopqrstuvwxyz letters: Available
a letter: a guess Please
_ a_ _ guess: Good
------------
left. guesses 8 have You
bcdefghijklmnopqrstuvwxyz letters: Available
a letter: a guess Please
_ a_ _ letter: that guessed already You've Oops!
------------
left. guesses 8 have You
bcdefghijklmnopqrstuvwxyz letters: Available
s letter: a guess Please
_ a_ _ word: my in not is letter That Oops!
------------
left. guesses 7 have You
bcdefghijklmnopqrtuvwxyz letters: Available
t letter: a guess Please
t ta_ guess: Good
------------
left. guesses 7 have You
bcdefghijklmnopqruvwxyz letters: Available
r letter: a guess Please
t ta_ word: my in not is letter That Oops!
------------
left. guesses 6 have You
bcdefghijklmnopquvwxyz letters: Available
m letter: a guess Please
t ta_ word: my in not is letter That Oops!
------------
left. guesses 5 have You
bcdefghijklnopquvwxyz letters: Available
c letter: a guess Please
tact guess: Good
------------
won! you Congratulations,

this... like look should game losing a of output the And
file... from list word Loading
loaded. words 55900
Hangman! game the to Welcome
long letters 4 is that word a of thinking am I
-----------
left guesses 8 have You
abcdefghijklmnopqrstuvwxyz Letters: Available
a letter: a guess Please
_ _ _ _ word: my in not is letter That Oops!
-----------
left guesses 7 have You
bcdefghijklmnopqrstuvwxyz Letters: Available
b letter: a guess Please
_ _ _ _ word: my in not is letter That Oops!
-----------
left guesses 6 have You
cdefghijklmnopqrstuvwxyz Letters: Available
c letter: a guess Please
_ _ _ _ word: my in not is letter That Oops!
-----------
left guesses 5 have You
defghijklmnopqrstuvwxyz Letters: Available
d letter: a guess Please
_ _ _ _ word: my in not is letter That Oops!
-----------
left guesses 4 have You
efghijklmnopqrstuvwxyz Letters: Available
e letter: a guess Please
e _ e_ guess: Good
-----------
left guesses 4 have You
fghijklmnopqrstuvwxyz Letters: Available
f letter: a guess Please
e _ e_ word: my in not is letter That Oops!
-----------
left guesses 3 have You
ghijklmnopqrstuvwxyz Letters: Available
g letter: a guess Please
e _ e_ word: my in not is letter That Oops!
-----------
left guesses 2 have You
hijklmnopqrstuvwxyz Letters: Available
h letter: a guess Please
e _ e_ word: my in not is letter That Oops!
-----------
left guesses 1 have You
ijklmnopqrstuvwxyz Letters: Available
i letter: a guess Please
e _ e_ word: my in not is letter That Oops!
-----------
else. was word The guesses. of out ran you Sorry,


isWordGuessed, functions helper the use to choose you if that Note
your paste to need not do you getAvailableLetters, or getGuessedWord,
these of implementations our supplied have We box. the in definitions
additional use you If problem. the of part this in use your for functions
here. definitions those paste to need will you functions, helper

guess. user's the get to raw_input to calls include should function Your

Places? Various at None Have Output my does Why
the printing are you that fact the from comes it and keyword a is None
example: For anything. return not does that function a of result
foo(x): def
x print

output: see will you foo(3), with function the call just you If
variable the printed function the because #-- 3

output: see will you foo(3), print do you if However,
variable the printed function the because #-- 3
return) the hence (and function the printed you because #-- None

return not does write you function a If something. return functions All
default the then console), the to something prints just (and anything
None return to is Python in action

"""

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
                

# rewrite 1
def hangman(secretWord):

    import string

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'

    num_guess = 8
    cnt = 8
    label = True
    lettersGuessed = []

    while label and cnt > 0:
        print '-------------'
        print 'You have ' + str(cnt) + ' guesses left.'
        print 'Available letters: ' +  getAvailableLetters(lettersGuessed)
        
        guessed_word = getGuessedWord(secretWord, lettersGuessed)

        guess = raw_input('Please guess a letter: ')

        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + guessed_word
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                guessed_word = getGuessedWord(secretWord, lettersGuessed)
                print 'Good guess: ' + guessed_word
                #if guessed_word == secretWord:
                if isWordGuessed(secretWord, lettersGuessed):
                    print '------------'
                    print 'Congratulations, you won!'
                    label = False
            else:
                print 'Oops! That letter is not in my word: ' + guessed_word
                cnt -= 1

    if label == True and cnt == 0:
        print '------------'
        print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
        
