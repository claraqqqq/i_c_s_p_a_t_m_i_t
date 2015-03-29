# ALPHABETICAL SUBSTRINGS  (15/15 points)

'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 

For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements or define the variable s in any way. 
Our automated testing will provide a value of s for you - 
so the code you submit in the following box should assume s is already defined. 
If you are confused by this instruction, please review L4 Problems 10 and 11 before 
you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you 
move on to a different part of the course. If you have time, come back to 
this problem after you've had a break and cleared your head.

'''

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

