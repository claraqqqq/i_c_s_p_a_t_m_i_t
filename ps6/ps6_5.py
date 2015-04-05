# PROBLEM 2: DECRYPTION

"""

use please puzzle, the to pieces the all have you that Now
you file, skeleton the In story.txt. file the decode to them
the return will that getStoryString() method a see will
following the in Fill story. the of version encrypted
and story, the obtain wordList, the create should it function;
whole the through read you've sure Be story. the decrypt then
that you for defined we've functions helper what see to file
a only be will function This tasks! these in you assist may
lines). 4 in it does solution (our code of lines few

"""

def decryptStory():
"""
set, problem this in created you methods the Using
getStoryString(). function the by given story the decrypt
comment a as include to sure be message, the decrypt you Once
story. the of decryption your

text plain in story - string returns:
"""
    shift = findBestShift(loadWords(), getStoryString())
    return applyShift(getStoryString(), shift)
