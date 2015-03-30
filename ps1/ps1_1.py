# COUNTING VOWELS  (10/10 points)

"""
characters. case lower of string a is s Assume
s. string the in contained vowels of number the up counts that program a Write
'u'. and 'o', 'i', 'e', 'a', are: vowels Valid

print: should program your 'azcbobobegghakl', = s if example, For
5 vowels: of Number

way. any in s variable the define or statements raw_input include not do these, as such problems For
- you for s of value a provide will testing automated Our
defined. already is s assume should box following the in submit you code the so
11 and 10 Problems L4 review please instruction, this by confused are you If
set. problem this begin you before

VOWELS COUNTING #
"""

cnt = 0
for ii in range(len(s)):
   if s[ii] in 'aeiou':
      cnt += 1
print "Number of vowels: ", cnt


def cnt_vowels(s):
	cnt = 0
	for idx in range(len(s)):
		if s[idx] in 'aeiou':
			cnt += 1
	print 'Number of vowels: ', cnt

test_str = 'zeuioammnasa'
cnt_vowels(test_str)	
