# PROBLEM 1: ENCRYPTION 

"""
to coder a applies which applyCoder, function the define Next,
text. of string a

Cases Test

buildCoder(3)) world!", applyCoder("Hello, >>>
zruog!' 'Khoor,
buildCoder(23)) zruog!", applyCoder("Khoor, >>>
world!' 'Hello,

"""

def applyCoder(text, coder):
"""
text. encoded the Returns text. the to coder the Applies

string text:
characters shifted to characters of mappings with dict coder:
text original to chars coder mapping after text returns:
"""
    import string
    non_letter = string.punctuation + ' ' + string.digits
    valid_letter = string.ascii_uppercase + string.ascii_lowercase
    res = ''
    for letter in text:
        if letter not in non_letter:
            res += coder[letter]
        else:
            res += letter
    return res


