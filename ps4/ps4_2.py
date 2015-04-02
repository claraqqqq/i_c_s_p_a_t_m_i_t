# DEALING WITH HANDS 

"""
problem this of majority The entirely!!** problem this read **Please
useful incredibly an is which code, read to how learning of consists
function. short a implement will you end, the At skill. important and
but easy, seem may it - problem this on time your take to sure Be
an is this and challenging be can code else's someone reading
exercise. important

HANDS REPRESENTING

The game. the during player a by held letters of set the is hand A
the example, For letters. random of set a dealt initially is player
In l. i, u, m, l, q, a, hand: following the with out start could player
are keys the dictionary: a as represented be will hand a program, our
the times of number the are values the and letters (lowercase)
above the example, For hand. that in repeated is letter particular
as: represented be would hand

'i':1} 'u':1, 'm':1, 'l':2, 'q':1, {'a':1, = hand
a with that Remember represented. is 'l' letter repeated the how Notice
is 'a' where hand['a'], is value a access to way usual the dictionary,
in is key the if works only this However, find. to want we key the
use can we this, avoid To KeyError. a get we otherwise, dictionary; the
if value a access to way "safe" the is This hand.get('a',0). call the
d.get(key,default) dictionary. the in is key the sure not are we
default. else d, dictionary the in is key if key for value the returns
never method this that so None, returns it given, not is default If
example: For KeyError. a raises

hand['e'] >>>
last): call recent (most Traceback
<module> in 1, line "<stdin>", File
'e' KeyError:
0) hand.get('e', >>>
0
REPRESENTATION DICTIONARY INTO WORDS CONVERTING


defined getFrequencyDict, is you for defined we've function useful One
it input, an as letters of string a given When ps4a.py. of top the near
the are values the and letters are keys the where dictionary a returns
For string. input the in represented is letter that times of number
example:

getFrequencyDict("hello") >>>
1} 'o': 2, 'l': 1, 'e': 1, {'h':
represent to use we dictionary of kind same the is this see, can you As
hands.

HAND A DISPLAYING

a in it display to want we dictionary, a as represented hand a Given
the in this for implementation the provided have We way. user-friendly
this through read to now right minutes few a Take function. displayHand
works. it how and does it what understand and carefully function

HAND RANDOM A GENERATING

We random. at chosen letters of set a is dealt is player a hand The
this generates that function a of implementation the with you provide
integer positive a input as takes function The dealHand. hand, random
letters. lowercase n containing hand a object, new a returns and n,
function this through read to now!) (right minutes few a take Again,
works. it how and does it what understand and carefully

THIS) IMPLEMENT (YOU HAND A FROM LETTERS REMOVING

spells player the As letters. of set a hand, a with starts player The
player the example, For up. used are set this from letters words, out
The l. i, u, m, l, q, a, hand: following the with out start could
the leave would This . quail word the spell to choose could player
implement to is task Your m. l, hand: player's the in letters following
( word a and hand a - inputs two in takes which updateHand, function the
and word, the spell to hand the from letters uses updateHand string).
remaining. letters the only containing hand, the of copy a returns then
example: For

'i':1} 'u':1, 'm':1, 'l':2, 'q':1, {'a':1, = hand >>>
you for Implemented # displayHand(hand) >>>
i u m l l q a
function! this implement You # 'quail') updateHand(hand, = hand >>>
hand >>>
'i':0} 'u':0, 'm':1, 'l':1, 'q':0, {'a':0,
displayHand(hand) >>>
m l
side no has function this sure Make function. updateHand the Implement
pasting Before in. passed hand the mutate not must it i.e., effects:
appropriate the passed you've sure be here, definition function your
test_ps4a.py. in tests

Hints
Testing
also will You pass. tests test_updateHand() the sure Make Testing:
reasonable some with updateHand of implementation your test to want
inputs.
Dictionaries Copying
( dictionaries Python of method ".copy" the review to wish may You
here). methods dictionary Python other and this review

of lines 4 is (ours short be should updateHand of implementation Your
functions. helper any call to need not does It code).

to go ps4a.py in code modify you If instructions: specific Canopy

keyboard) your on dot the with CTRL the hit (or Kernel Restart -> Run

modify you time every this do to have You test_ps4a.py. running before
latter. the in incorporated be not will former the to changes otherwise test_ps4a.py, file the run to want and ps4a.py file the

"""


def updateHand(hand, word):

"""
word. in letters the all has 'hand' that Assumes
times many however that assumes this words, other In
as least at has 'hand' 'word', in appears letter a
it. in letter that of many

word given the in letters the up uses hand: the Updates
it. in letters those without hand, new the returns and

hand. modify not does effects: side no Has

string word:
int) -> (string dictionary hand:
int) -> (string dictionary returns:
"""
    
    label = True
    for letter in word:
        if hand[letter] <= 0:
            label = False
    if label == False:
        return hand
    else:
        for letter in word:
            hand[letter] -= 1
    return hand

