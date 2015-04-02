# WORD SCORES 

"""
to us allows that code some implement to is step first The
function The word. single a for score the calculate
lowercase of string a input as accept should getWordScore
word, that for score integer the return and word) (a letters
rules. scoring game's the using

Rules Scoring the of Reminder A
Scoring
word each for scores the of sum the is hand the for score The
formed.
in letters for points the of sum the is word a for score The
points 50 plus word, the of length the by multiplied word, the
created. word first the on used are letters n all if
3, worth is B 1, worth is A Scrabble; in as scored are Letters
have We on. so and 1, worth is E 2, worth is D 3, worth is C
each maps that SCRABBLE_LETTER_VALUES dictionary the defined
value. letter Scrabble its to letter lowercase
for ((4+1+1+2) points 32 worth be would 'weed' example, For
get to len('weed') by multiply then letters, four the
actually hand the that check to sure Be 32). = (4+1+1+2)*4
word! the scoring before 'd' 1 and 'e's, 2 'w', 1 has
on 'waybill' word the make you and n=7 if example, another As
score base (the points 155 worth be would it try, first the
additional an plus (4+1+4+3+1+1+1)*7=105, is 'waybill' for
letters). n all using for bonus point 50

HINTS

string a either always is word input the that assume may You
"". string empty the or letters, lowercase of
dictionary SCRABBLE_LETTER_VALUES the use to want will You
value. its change not should You ps4a.py. of top the at defined
The hand! a in letters 7 always are there that assume not Do
score bonus a for required letters of number the is n parameter
to is goal Our hand). the in letters of number maximum (the
word your playing try to want you if - modular code the keep
simply by it do to able be will you n=4, or n=10 with game
HAND_SIZE! of value the changing
you and properly, implemented is function this If Testing:
test_getWordScore() the that see should you test_ps4a.py, run
getWordScore, of implementation your test Also pass. tests
words. English reasonable some using
you've sure be and ps4a.py in getWordScore for code the in Fill
pasting before test_ps4a.py in tests appropriate the passed
here. definition function your

ps4a.py in code modify you If instructions: specific Canopy
to go

your on dot the with CTRL the hit (or Kernel Restart -> Run
keyboard)

time every this do to have You test_ps4a.py. running before
file the run to want and ps4a.py file the modify you
be not will former the to changes otherwise test_ps4a.py,
latter. the in incorporated

"""

def getWordScore(word, n):
"""
valid a is word the Assumes word. a for score the Returns
word.

letters for points the of sum the is word a for score The
50 PLUS word, the of length the by multiplied word, the in
turn. first the on used are letters n all if points

3, worth is B 1, worth is A Scrabble; in as scored are Letters
on so and 1, worth is E 2, worth is D 3, worth is C
SCRABBLE_LETTER_VALUES) (see

letters) (lowercase string word:
points) additional for required size hand i.e., (HAND_SIZE; integer n:
0 >= int returns:
"""
    res = 0
    for letter in word:
    	res += SCRABBLE_LETTER_VALUES[letter]
    res *= len(word)
    if len(word) == n:
    	res += 50
    return res


