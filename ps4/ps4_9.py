# YOU AND YOUR COMPUTER  (1 point possible)

"""
computer the give to need you word, a choose can computer your that Now
playGame the re-implements that code the Write play. to option the
in below described as behave to function the modify will You function.
HAND_SIZE the use should you before, As comments. function's the
out try to sure Be hand. a in cards of number the determine to constant
program. your with HAND_SIZE for values different

Hints and Output Sample
look... should output game the how is Here
end to e or hand, last the replay to r hand, new a deal to n Enter
n game:

u play: computer the have to c play, yourself have to u Enter

t t t e r s a Hand: Current
tatters finished: are you that indicate to "." a or word, Enter
points 99 Total: points. 99 earned "tatters"

points. 99 score: Total letters. of out Run

end to e or hand, last the replay to r hand, new a deal to n Enter
r game:

c play: computer the have to c play, yourself have to u Enter

t t t e r s a Hand: Current
points 99 Total: points. 99 earned "stretta"

points. 99 score: Total

end to e or hand, last the replay to r hand, new a deal to n Enter
x game:
command. Invalid

end to e or hand, last the replay to r hand, new a deal to n Enter
n game:

me play: computer the have to c play, yourself have to u Enter
command. Invalid

you play: computer the have to c play, yourself have to u Enter
command. Invalid

c play: computer the have to c play, yourself have to u Enter

n l x d e c a Hand: Current
points 65 Total: points. 65 earned "axled"

n c Hand: Current
points. 65 score: Total

end to e or hand, last the replay to r hand, new a deal to n Enter
n game:

u play: computer the have to c play, yourself have to u Enter

o z h h y p a Hand: Current
zap finished: are you that indicate to "." a or word, Enter
points 42 Total: points. 42 earned "zap"

o h h y Hand: Current
oy finished: are you that indicate to "." a or word, Enter
points 52 Total: points. 10 earned "oy"

h h Hand: Current
. finished: are you that indicate to "." a or word, Enter
points. 52 score: Total Goodbye!

end to e or hand, last the replay to r hand, new a deal to n Enter
r game:

c play: computer the have to c play, yourself have to u Enter

o z h h y p a Hand: Current
points 80 Total: points. 80 earned "hypha"

o z Hand: Current
points. 80 score: Total

end to e or hand, last the replay to r hand, new a deal to n Enter
e game:
output the about Hints
is little very - carefully output sample above the inspect to sure Be
printed the of Most specifically. function this in out printed actually
and playHand in wrote you code the from comes actually output
function uses and modular is code your that sure be - compPlayHand
functions! helper these to calls
You function. helper dealHand the to calls make also should You
so written we've that function helper other any to calls make shouldn't
code of lines 15-20 about in written be can function this fact, in - far
.
and playHand from output the with output, above the is Here
obscured: compPlayHand
end to e or hand, last the replay to r hand, new a deal to n Enter
n game:

u play: computer the have to c play, yourself have to u Enter

playHand> to <call

end to e or hand, last the replay to r hand, new a deal to n Enter
r game:

c play: computer the have to c play, yourself have to u Enter

compPlayHand> to <call

end to e or hand, last the replay to r hand, new a deal to n Enter
x game:
command. Invalid

end to e or hand, last the replay to r hand, new a deal to n Enter
n game:

me play: computer the have to c play, yourself have to u Enter
command. Invalid

you play: computer the have to c play, yourself have to u Enter
command. Invalid

c play: computer the have to c play, yourself have to u Enter

compPlayHand> to <call

end to e or hand, last the replay to r hand, new a deal to n Enter
n game:

u play: computer the have to c play, yourself have to u Enter

playHand> to <call

end to e or hand, last the replay to r hand, new a deal to n Enter
r game:

c play: computer the have to c play, yourself have to u Enter

compPlayHand> to <call

end to e or hand, last the replay to r hand, new a deal to n Enter
e game:
approachable. more bit a seem problem the makes hint this Hopefully
Runtime On Note A
is This plays. computer the when slowly run things that notice may You
to free feel optional!), (totally want you If expected. be to
is way one - faster go turn computer's the making of ways investigate
so int) -> (string dictionary a into list word the preprocess to
the in faster much becomes word a of score the up looking
function. compChooseWord
- time one preprocessing this do to want only you - though careful Be
of bottom the (at you for wordList the generate we after right probably
inputs what modify to have you'll this, do to choose you If file). the
of instead dictionary word a take probably (they'll take functions your
example). for list, word a
the in code your running when issue this about worry IMPORTANT:Don't
than smaller (much wordList sample small very a load We below! checker
work will code Your out. time code your having avoid to words!) 83667
described. as pre-processing of form a implement don't you if even
Code Your Entering
the in ps4b.py from playGame for definition your paste only to sure Be
definitions. function other any include not Do box. following

"""

def playGame(wordList):
"""
hands. of number arbitrary an play to user the Allow

'e'. or 'r' or 'n' input to user the Asks 1)
game. the exit immediately 'e', inputs user the If *
again. them asking keep 'e', or 'r', 'n', not that's anything inputs user the If *

'c'. a or 'u' a input to user the Asks 2)
again. them asking keep 'u', or 'c' not that's anything inputs user the If *

choices: above the on based functionality Switch 3)
hand. (random) new a play 'n', inputted user the If *
again. hand last the play 'r', inputted user the if Else, *

game the play user the let 'u', inputted user the If *
playHand. using hand, selected the with
the play computer the let 'c', inputted user the If *
compPlayHand. using hand, selected the with game

1 step from repeat hand, the played has user or computer the After 4)

(string) list wordList:
"""
    label1 = True

    cnt = 0

    while label1:
        choice1 = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        label2 = True
        if choice1 == 'n':     
            hand = dealHand(HAND_SIZE)
            hand_copy = hand.copy()
            while label2:     
                choice2 = raw_input('Enter u to have yourself play, c to have the computer play: ')         
                if choice2 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    cnt += 1
                    label2 = False
                elif choice2 == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    cnt += 1
                    label2 = False
                else:    
                    print 'Invalid command.'
        
        elif choice1 == 'r':
            if cnt == 0:
                print 'You have not played a hand yet. Please play a new hand first!' 
            else:
                hand = hand_copy.copy()
                while label2:                       
                    choice2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if choice2 == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        label2 = False
                    elif choice2 == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        label2 = False
                    else:    
                        print 'Invalid command.'
                
        elif choice1 == 'e':
            label1 = False
            
        else:
            print 'Invalid command.'



