# HAND LENGTH

"""
interacts that code the writing begin to ready now are We
playHand the implementing be We'll player. the with
a out play to user the allows function This function.
the implement to need you'll though, First, hand. single
in done be can which function, calculateHandlen helper
code. of lines five under
"""
def calculateHandlen(hand):
"""
hand. current the in letters) of (number length the Returns

int) (string dictionary hand:
integer returns:
"""
    res = 0
    for key in hand.keys():
        res += hand[key]
    return res



