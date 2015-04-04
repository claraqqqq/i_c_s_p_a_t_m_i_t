# COMPUTER PLAYS A HAND 

"""
we word, a choose computer the let to ability the have we that Now
- hand a play to computer the allow to function a up set to need
the (get function playHand A's Part to similar very manner a in
hint?).

allow should function This function. compPlayHand the Implement
just you procedure the using hand, given a play to computer the
the to similar very be should This part. previous the in wrote
although word, the selected user a which in version earlier
be will hand particular a playing done is it when deciding
different.

hands generated randomly some on function your test to sure Be
dealHand. using

Cases Test
Cases Test
a finds code your if okay is it Note at. look to cases test Some
same. the are values point the as long as word, different
6) wordList, 1}, 'l': 1, 'e': 1, 's': 2, 'p': 1, compPlayHand({'a':
l e s p p a Hand: Current
points 110 Total: points. 110 earned "appels"
points. 110 score: Total
5) wordList, 1}, 't': 1, 'b': 1, 'c': 2, compPlayHand({'a':
t b c a a Hand: Current
points 24 Total: points. 24 earned "acta"

b Hand: Current
points. 24 score: Total
2}, 't': 2, 'n': 2, 'm': 2, 'i': 2, 'e': 2, compPlayHand({'a':
12) wordList,
t t n n m m i i e e a a Hand: Current
points 96 Total: points. 96 earned "immanent"

i t e a Hand: Current
points 105 Total: points. 9 earned "ait"

e Hand: Current
points. 105 score: Total
surround must you correctly, graded be to code your For Important:
when So quotes. double or single with word computer's the
look should line your chooses computer the word what displaying
like:
points 96 Total: points. 96 earned "immanent"
or
points 96 Total: points. 96 earned 'immanent'

your to addition in compChooseWord, of definition your Paste
below. box the in compPlayHand, of definition

"""


def compPlayHand(hand, wordList, n):
"""
procedure same the following hand, given the play to computer the Allows
computer the word, a choosing user the of instead except playHand, as
it. chooses

displayed. is hand The 1)
word. a chooses computer The 2)
is word that for score the and word the word: valid every After 3)
the and displayed, are hand the in letters remaining the displayed,
word. another chooses computer
finishes. hand the when displayed is scores word the of sum The 4)
possible its exhausted has computer the when finishes hand The 5)
None). returns compChooseWord (i.e. choices

int) -> (string dictionary hand:
(string) list wordList:
points) additional for required size hand i.e., (HAND_SIZE; integer n:
"""
    
    def compChooseWord(hand, wordList, n):  
        score_best = 0
        score_current = 0  
        word_best = ''
        for word in wordList:
            if isValidWord(word, hand, wordList):
                score_current = getWordScore(word, n)
                if score_current > score_best:
                    score_best = score_current    
                    word_best = word
        if word_best == '':
            return None
        else:
            return word_best
    
    score_current = 0
    score_total = 0
    label = True
    while label:
        print 'Current Hand: ',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word != None:
            hand = updateHand(hand, word)
            score_current = getWordScore(word, n)
            score_total += score_current
            print '"'+word+'" earned '+str(score_current)+' points. Total: '+str(score_total)+' points'
            if calculateHandlen(hand) == 0: 
                label = False
        else:
            label = False
    print 'Total score: '+str(score_total)+' points.'            

