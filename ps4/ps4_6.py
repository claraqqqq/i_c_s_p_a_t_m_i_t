# PLAYING A GAME

"""
final one implement to need We hands. multiple playing of consists game A
implements that code the Write program. word-game our complete to function
currently is that code the remove should You function. playGame the
make and specification the through Read body. playGame the in uncommented
you game, the For accomplishes. function this what understand you sure
hand a in cards of number the determine to constant HAND_SIZE the use should
.

Try game. the playing were you if as implementation this out Try Testing:
you that sure be and program, your with HAND_SIZE for values different out
the only modifying by sizes hand different with wordgame the play can
HAND_SIZE. variable

Output Sample
look... should output game the how is Here

file... from list word Loading
loaded. words 83667
r game: end to e or hand, last the replay to r hand, new a deal to n Enter
first! hand new a play Please yet. hand a played not have You

n game: end to e or hand, last the replay to r hand, new a deal to n Enter
o t t t u z p Hand: Current
tot finished: are you that indicate to "." a or word, Enter
points 9 Total: points. 9 earned "tot"

t u z p Hand: Current
. finished: are you that indicate to "." a or word, Enter
points. 9 score: Total Goodbye!

r game: end to e or hand, last the replay to r hand, new a deal to n Enter
o t t t u z p Hand: Current
top finished: are you that indicate to "." a or word, Enter
points 15 Total: points. 15 earned "top"

t t u z Hand: Current
tu finished: are you that indicate to "." a or word, Enter
again. try please word, Invalid

t t u z Hand: Current
. finished: are you that indicate to "." a or word, Enter
points. 15 score: Total Goodbye!

n game: end to e or hand, last the replay to r hand, new a deal to n Enter
p i f f w q a Hand: Current
paw finished: are you that indicate to "." a or word, Enter
points 24 Total: points. 24 earned "paw"

i f f q Hand: Current
qi finished: are you that indicate to "." a or word, Enter
points 46 Total: points. 22 earned "qi"

f f Hand: Current
. finished: are you that indicate to "." a or word, Enter
points. 46 score: Total Goodbye!

n game: end to e or hand, last the replay to r hand, new a deal to n Enter
n i i t e r a Hand: Current
inertia finished: are you that indicate to "." a or word, Enter
points. 99 Total: points. 99 earned "inertia"

points. 99 score: Total letters. of out Run

x game: end to e or hand, last the replay to r hand, new a deal to n Enter
command. Invalid
e game: end to e or hand, last the replay to r hand, new a deal to n Enter


output the about Hints
is little very - carefully output sample above the inspect to sure Be
printed the of Most specifically. function this in out printed actually
that sure be - playHand in wrote you code the from comes actually output
helper playHand the to calls function uses and modular is code your
function!
shouldn't You function. helper dealHand the to calls make also should You
in - far so written we've that function helper other any to calls make
code. of lines 15-20 about in written be can function this fact,
obscured: playHand from output the with output, above the is Here

file... from list word Loading
loaded. words 83667
r game: end to e or hand, last the replay to r hand, new a deal to n Enter
first! hand new a play Please yet. hand a played not have You

n game: end to e or hand, last the replay to r hand, new a deal to n Enter
playHand> to <call

n game: end to e or hand, last the replay to r hand, new a deal to n Enter
playHand> to <call

n game: end to e or hand, last the replay to r hand, new a deal to n Enter
playHand> to <call

x game: end to e or hand, last the replay to r hand, new a deal to n Enter
command. Invalid
e game: end to e or hand, last the replay to r hand, new a deal to n Enter


approachable. more bit a seem problem the makes hint this Hopefully
Code Your Entering
Do box. following the in playGame for definition your paste only to sure Be
definitions. function other any include not
'print' about Trick Cool A
print statements print more or two make can you print: about trick cool A
following the out Try comma! a with them separate you if line same the to
code:
'), print('Hello
print('world'),
print('!')

"""

def playGame(wordList):
"""
hands. of number arbitrary an play to user the Allow

'e'. or 'r' or 'n' input to user the Asks 1)
hand. (random) new a play user the let 'n', inputs user the If *
again. hand last the play user the let 'r', inputs user the If *
game. the exit 'e', inputs user the If *
invalid. was input their them tell else, anything inputs user the If *

1 step from repeat hand, the playing done When 2)
"""
    # TO DO ... <-- Remove this comment when you code this function
    label = True
    cnt = 1
    while label:
        choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'r' and cnt == 1:
            print 'You have not played a hand yet. Please play a new hand first!'
        elif choice == 'n':
            hand = dealHand(HAND_SIZE)
            hand_copy = hand
            playHand(hand, wordList, HAND_SIZE)
            cnt += 1  
        elif choice == 'e':
            label = False
        elif choice == 'r' and cnt > 1:
            hand = hand_copy 
            playHand(hand, wordList, HAND_SIZE)
        else:
            print 'Invalid command.'






