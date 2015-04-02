# VALID WORDS  

"""
random a generate to code written have we point, this At
ask also can We user. the to hand that display and hand
the score and raw_input) (Python's word a for user the
we point this at However, getWordScore). your (using word
by given word a that verify to code any written not have
in is word valid A game. the of rules the obeys player a
letters of entirely composed is it and list; word the
function. isValidWord the Implement hand. current the from

In pass. tests test_isValidWord the sure Make Testing:
by implementation your test to want will you addition,
should what - hand same the on times multiple it calling
( string empty the Additionally, be? behavior correct the
function this code you if - word valid a not is '')
for check additional an need shouldn't you correctly,
condition. this

sure be and ps4a.py in isValidWord for code the in Fill
test_ps4a.py in tests appropriate the passed you've
here. definition function your pasting before

ps4a. in code modify you If instructions: specific Canopy
to go py


dot the with CTRL the hit (or Kernel Restart -> Run
keyboard) onyour

every this do to have You test_ps4a.py. running before
file the run to want and ps4a.py file the modify you time
be not will former the to changes otherwise test_ps4a.py,
latter. the in incorporated
"""

def isValidWord(word, hand, wordList):
"""
entirely is and wordList the in is word if True Returns
False. returns Otherwise, hand. the in letters of composed

wordList. or hand mutate not Does

string word:
int) -> (string dictionary hand:
strings lowercase of list wordList:
"""
    label_inWordList = False
    if word in wordList:
        label_inWordList = True
        
    label = True
    hand_copy = hand.copy()
    for letter in word:
        if letter not in hand_copy.keys():
            label = False
        elif hand_copy[letter] < 1:
            label = False
        else:
            hand_copy[letter] -= 1
            
    return label and label_inWordList

            
