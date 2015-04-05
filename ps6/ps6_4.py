# PROBLEM 2: DECRYPTION

"""
excited really is 6.00.1x, taking also is who friend, Your
set. problem this of 1 Problem for wrote she program the about
the with encrypted all they're but emails, you sends She
cipher! Caesar

her decrypting then using, is she key shift which know you If
the is message string the If task. easy an is message
then using, is she key shift the is k and message encrypted
message. original her returns 26-k) applyShift(message, calling
why? see you Do

using. is she key shift which know don't you is, problem The
writes and speaks only friend your know you is, news good The
the find to program a write can you if So words. English
English real of number maximum the produces that decoding
(there's decoding right the find probably can you words,
Accounting unique. be not may shift the that chance a always
require won't we that methods statistical use would this for
you.) of

PSEUDOCODE

pseudocode! some write to time take should you now, Right
problem this solve to use could you algorithm an about Think
algorithm your verify can you Then, down. steps the write and
coding. before ps6_pseudo.txt in pseudocode supplied the with

pseudocode, your checking and writing done you've After
and wordList a takes function This findBestShift(). implement
that shift the find to attempts and text encrypted of sample a
the not or whether of indication simple A text. the encoded
obtained words the of most if is found been has shift correct
that means only this that Note words. valid are shift a after
to possible is It words. actual are obtained words the of most
into shifts separate two by decoded be can that message a have
strategies various are there While words. of sets different
problem this for decryptions, ambiguous between deciding for
solution. simple a for looking only are we

a provided have we problem, this solving in you assist To
simply This word). isWord(wordList, function, helper
wordList. the to according word valid a is word if determines
punctuation. and capitalization ignores function This

Hints
string.split Using
the dividing for useful string.split function the find may You
words. into up text
world!'.split('o') 'Hello >>>
'rld!'] w', ' ['Hell',
') fun'.split(' pretty is '6.00.1x >>>
'fun'] 'pretty', 'is', ['6.00.1x',
Cases Test
8) world!', applyShift('Hello, = s >>>
s >>>
ewztl!' 'Pmttw,
s) findBestShift(wordList, >>>
18
18) applyShift(s, >>>
world!' 'Hello,

"""

def findBestShift(wordList, text):
"""
text. encoded the decrypt can that key shift a Finds

string text:
26 < int <= 0 returns:
"""
    ### TODO

    import string
    shift_bestmatch = 0
    cnt_bestmatch = 0
    for shift in range(26):
        text_reverse = applyShift(text, shift)
        text_list = text_reverse.split(' ')
        cnt = 0
        for word in text_list:
            if isWord(wordList, word):
                cnt += 1
        if cnt > cnt_bestmatch:
            shift_bestmatch = shift
            cnt_bestmatch = cnt
    return shift_bestmatch            
    
        
        