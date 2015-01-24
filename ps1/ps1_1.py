# COUNTING VOWELS  

s = 'zeuioammnasa'
cnt = 0
for ii in range(len(s)):
   if s[ii] in 'aeiou':
      cnt += 1
print "Number of vowels: ", cnt
