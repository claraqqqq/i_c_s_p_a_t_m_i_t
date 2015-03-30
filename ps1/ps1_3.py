# ALPHABETICAL SUBSTRINGS  (15/15 points)

"""
characters. case lower of string a is s Assume

letters the which in s of substring longest the prints that program a Write
order. alphabetical in occur

print should program your then 'azcbobobegghakl', = s if example, For
beggh is: order alphabetical in substring Longest

substring. first the print ties, of case the In

print should program your then 'abcbcd', = s if example, For
abc is: order alphabetical in substring Longest

way. any in s variable the define or statements raw_input include not do these, as such problems For
- you for s of value a provide will testing automated Our
defined. already is s assume should box following the in submit you code the so
before 11 and 10 Problems L4 review please instruction, this by confused are you If
set. problem this begin you

smart. work to you encourage We challenging. fairly is problem This Note:
you that suggest we problem, this on hours few a than more spent you've If
to back come time, have you If course. the of part different a to on move
head. your cleared and break a had you've after problem this

"""

# ALPHABETICAL SUBSTRINGS
# s = 'kpxiaxnrjqfpfgwo'

# solution 1
cnt_longest = 0
cnt_tmp = 1
std = 0
stop = 0
char_first = s[0]
str_tmp = char_first 
str_longest = char_first
for index in range(len(s)-1):
   char_next = s[index+1]
   if char_first <= char_next:
      char_first = char_next
      str_tmp += char_next
      cnt_tmp += 1
      if cnt_longest < cnt_tmp:
         cnt_longest = cnt_tmp
         str_longest = str_tmp
   else:
      char_first = char_next
      str_tmp = char_next 
      cnt_tmp = 1

print "Longest substring in alphabetical order is: ", str_longest

# solution 2
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest

# solution 2 function
def alpha_substr(s):
   str_current = s[0]
   str_longest = s[0]
   for idx in range(1, len(s)):
      if s[idx] >= str_current[-1]:
         str_current += s[idx]
         if len(str_current) > len(str_longest):
            str_longest = str_current
      else:
         str_current = s[idx]
   print 'Longest substring in alphabetical order is:', str_longest

