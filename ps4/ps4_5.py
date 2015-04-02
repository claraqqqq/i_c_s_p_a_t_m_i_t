# PLAYING A HAND

"""

provided is pseudocode This pseudocode. of bunch a is there playHand, function the in that note ps4a.py, In
the about more learn to resource Pseudocode? Why the out Check function. your writing in you guide help to
solution. your coding start you before Pseudocode of Why and What

of size the represents n parameter The hand! a in letters 7 be always will there that assume not Do Note:
hand. the

the playing were you if as implementation your out try box, answer the in code your testing Before Testing:
playHand: of output example some is Here game.

Cases Test
#1 Case
Call: Function
loadWords() = wordList
7) wordList, 'a':1}, 'm':2, 'z':1, 'c':1, 'i':1, playHand({'h':1,
Output:
z m m h i c a Hand: Current
him finished: are you that indicate to "." a or word, Enter
points 24 Total: points. 24 earned "him"

z m c a Hand: Current
cam finished: are you that indicate to "." a or word, Enter
points 45 Total: points. 21 earned "cam"

z Hand: Current
. finished: are you that indicate to "." a or word, Enter
points. 45 score: Total Goodbye!
#2 Case
Call: Function
loadWords() = wordList
7) wordList, 'f':1}, 'o':1, 'a':1, 't':2, 's':1, playHand({'w':1,
Output:
o f w t t s a Hand: Current
tow finished: are you that indicate to "." a or word, Enter
points 18 Total: points. 18 earned "tow"

f t s a Hand: Current
tasf finished: are you that indicate to "." a or word, Enter
again. try please word, Invalid

f t s a Hand: Current
fast finished: are you that indicate to "." a or word, Enter
points. 46 Total: points. 28 earned "fast"

points. 46 score: Total letters. of out Run
#3 Case
Call: Function
loadWords() = wordList
7) wordList, 'i':2}, 'r':1, 'a':1, 't':1, 'e':1, playHand({'n':1,
Output:
n i i t e r a Hand: Current
inertia finished: are you that indicate to "." a or word, Enter
points 99 Total: points. 99 earned "inertia"

points. 99 score: Total letters. of out Run
Testing Additional
values varying with conditions test basic same the test you tests, listed the to addition in that, sure Be
hand. the in letters of number the than smaller be never will n n. of

"""

def playHand(hand, wordList, n):

"""
follows: as hand, given the play to user the Allows

displayed. is hand The *
".") string (the period single a or word a input may user The *
playing done they're indicate to
asking displayed is message a and rejected, are words Invalid *
"." or word valid a enter they until word another choose to user the
hand. the from letters up uses it entered, is word valid a When *
displayed, is word that for score the word: valid every After *
user the and displayed, are hand the in letters remaining the
word. another input to asked is
finishes. hand the when displayed is scores word the of sum The *
user the or letters unused more no are there when finishes hand The *
"." a inputs

int) -> (string dictionary hand:
strings lowercase of list wordList:
points) additional for required size hand i.e., (HAND_SIZE; integer n:

"""
    
    label = True
    word = ''
    score_current = 0
    score_total = 0
    while label:
        print 'Current Hand: ',
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            label = False
            print 'Goodbye! Total score: ' + str(score_total) + ' points.'        
            break
        elif isValidWord(word, hand, wordList):
            score_current = getWordScore(word, n)
            hand = updateHand(hand, word)
            score_current = getWordScore(word, n)
            score_total += score_current
            print '"' + str(word) + '"' + ' earned ' + str(score_current) + ' points. Total: ' + str(score_total) + ' points'
            print
        else:
            print 'Invalid word, please try again.'
            print
        if calculateHandlen(hand) == 0:
            print 'Run out of letters. Total score: ' + str(score_total) + ' points.'
            label = False
            break

