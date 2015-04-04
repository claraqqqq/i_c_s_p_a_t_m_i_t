#COMPUTER CHOOSES A WORD 

"""
to sure be so ps4a.py, from functions your on dependent is B Part
ps4b.py** on working before ps4a.py complete

you that decide you code, game word your completed have you that Now
hidden (your game the play to (SkyNet) computer your enable to like would
human to inferior are computers that all for and once prove to is agenda
playHand the to modification a make will you B Part In intellect!)
that is idea The happen. to this enable will that A part from function
game the in succeed user a as you how compare to able be will you
performance. computer's the to compared

compChooseWord(hand, function the create to responsibility your is It
ps4b.py. file the in provided is Pseudocode n). wordList,

is that player computer a create you'll pseudocode, the follow you If
our following it implemented you've Once best. the always not but legal,
to love we'd as much As approach! own your try to free feel approach,
hope we function, compChooseWord improved an making for credit you give

their in limited are facilities grading automatic our understand can you
solutions. differing accept to ability

Output Sample and Hints
Runtime On Note A
This plays. computer the when slowly bit a run things that notice may You
all! after words, 83667 has wordList the - expected be to is
the in code your running when issue this about worry don't However,
than smaller (much wordList sample small very a load We below! checker
out. time code your having avoid to words!) 83667
Cases Test
at: look to cases test Some
6) wordList, 1}, 'l': 1, 'e': 1, 's': 2, 'p': 1, compChooseWord({'a': >>>
appels
5) wordList, 1}, 't': 1, 'b': 1, 'c': 2, compChooseWord({'a': >>>
acta
2}, 't': 2, 'n': 2, 'm': 2, 'i': 2, 'e': 2, compChooseWord({'a': >>>
12) wordList,
immanent
12) wordList, 2}, 't': 2, 'n': 2, 'q': 2, 'z': 2, compChooseWord({'x': >>>
None
on depending apples, find also might code your case test first the For
correct. as check will and okay is This solution. your code you how

"""

def compChooseWord(hand, wordList, n):
"""
gives that word the find wordList, a and hand a Given
it. return and score, value maximum the

words the all considering by calculated be should word This
wordList. the in

None. return hand, the from made be can wordList the in words no If

int) -> (string dictionary hand:
(string) list wordList:
None or string returns:
"""
    
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
            


