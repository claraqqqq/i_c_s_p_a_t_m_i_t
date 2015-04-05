# ENCRYPTION 

"""
strings. encode to them use to able be should you applyCoder, and buildCoder written have you Once

Cases Test

8) test.', a is applyShift('This >>>
bmab.' i qa 'Bpqa
18) bmab.', i qa applyShift('Bpqa >>>
test.' a is 'This

"""


def applyShift(text, shift):
"""
shift given the by shifted Caesar text new a returns text, a Given
case upper case, lower remain should letters case Lower offset.
should punctuation other all and case, upper remain should letters
is. it as stay

to shift the apply to string text:
26) < int <= (0 text the shift to amount shift:
amount. specified by shifted being after text returns:
"""
    ### TODO.
    ### HINT: This is a wrapper function.
    coder = buildCoder(shift)
    return applyCoder(text, coder)
