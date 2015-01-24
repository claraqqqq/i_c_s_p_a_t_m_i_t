# ALPHABETICAL SUBSTRINGS
s = 'kpxiaxnrjqfpfgwo'

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