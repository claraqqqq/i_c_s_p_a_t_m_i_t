# COUNTING BOBS

s = 'dbobbobblo'
cnt = 0
for ii in range(len(s)-2):
   test_string = s[ii]+s[ii+1]+s[ii+2]
   if test_string == 'bob':
      cnt += 1
print "Number of times bob occurs is: ", cnt