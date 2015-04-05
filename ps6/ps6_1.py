# PROBLEM 1: ENCRYPTION 

"""
into plaintext encrypt to program a write now You'll
cipher. Caesar the using ciphertext

to introduction the understood and read fully have you sure Be
problem! this

Hints
Letters Case Lower and Upper
upper and lower both includes dictionary your that sure Be
case lower a for character shifted the that but letters, case
case upper and lower are version uppercase its and letter
the if that is means this What letter. same the of instances
the "c", is value shifted its and "a" is letter original
"C". letter the to shift should "A" letter
the of characters or ordering the with unfamiliar are you If
ordering letter the following be will we alphabet, English
string.ascii_uppercase: and string.ascii_lowercase by displayed
string import >>>
string.ascii_lowercase print >>>
abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase print >>>
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ignore to Characters
the as such Characters - page introduction the from reminder A
will etc points, exclamation periods, commas, character, space
the all basically, - cipher this by encrypted be not
and ') (' space the plus string.punctuation, within characters
string.digits. in found 9) - (0 characters numerical all
Cases Test
buildCoder(3)
'J', 'G': 'G', 'D': 'H', 'E': 'E', 'B': 'F', 'C': 'D', {'A':
'P', 'M': 'M', 'J': 'N', 'K': 'K', 'H': 'L', 'I': 'I', 'F':
'V', 'S': 'S', 'P': 'T', 'Q': 'Q', 'N': 'R', 'O': 'O', 'L':
'B', 'Y': 'Y', 'V': 'Z', 'W': 'W', 'T': 'X', 'U': 'U', 'R':
'h', 'e': 'e', 'b': 'f', 'c': 'd', 'a': 'C', 'Z': 'A', 'X':
'n', 'k': 'k', 'h': 'l', 'i': 'i', 'f': 'j', 'g': 'g', 'd':
't', 'q': 'q', 'n': 'r', 'o': 'o', 'l': 'p', 'm': 'm', 'j':
'z', 'w': 'w', 't': 'x', 'u': 'u', 'r': 'v', 's': 's', 'p':
'c'} 'z': 'a', 'x': 'b', 'y': 'y', 'v':
buildCoder(9)
'P', 'G': 'M', 'D': 'N', 'E': 'K', 'B': 'L', 'C': 'J', {'A':
'V', 'M': 'S', 'J': 'T', 'K': 'Q', 'H': 'R', 'I': 'O', 'F':
'B', 'S': 'Y', 'P': 'Z', 'Q': 'W', 'N': 'X', 'O': 'U', 'L':
'H', 'Y': 'E', 'V': 'F', 'W': 'C', 'T': 'D', 'U': 'A', 'R':
'n', 'e': 'k', 'b': 'l', 'c': 'j', 'a': 'I', 'Z': 'G', 'X':
't', 'k': 'q', 'h': 'r', 'i': 'o', 'f': 'p', 'g': 'm', 'd':
'z', 'q': 'w', 'n': 'x', 'o': 'u', 'l': 'v', 'm': 's', 'j':
'f', 'w': 'c', 't': 'd', 'u': 'a', 'r': 'b', 's': 'y', 'p':
'i'} 'z': 'g', 'x': 'h', 'y': 'e', 'v':

"""

def buildCoder(shift):
"""
letter. a to cipher Caesar a apply can that dict a Returns
characters non-letter Ignores value. shift the by defined is cipher The
spaces. and numbers, punctuation, like

26 < int <= 0 shift:
dict returns:
"""
    import string
    str_lower = string.ascii_uppercase
    str_lower += str_lower
    str_upper = string.ascii_lowercase
    str_upper += str_upper
    res_lower = {}
    res_upper = {}
    for idx in range(26):
        res_lower[str_lower[idx]] = str_lower[idx + shift]
        res_upper[str_upper[idx]] = str_upper[idx + shift]
        
    res = dict(res_upper.items() + res_lower.items())
    # res = dict(res_upper)
    # res.update(str_lower)

    return res


