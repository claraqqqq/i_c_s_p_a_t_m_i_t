# COUNTING BOBS

"""
characters. case lower of string a is s Assume

s. in occurs 'bob' string the times of number the prints that program a Write
print should program your then 'azcbobobegghakl', = s if example, For
2 is: occurs bob times of Number

way. any in s variable the define or statements raw_input include not do these, as such problems For
- you for s of value a provide will testing automated Our
defined. already is s assume should box following the in submit you code the so
11 and 10 Problems L4 review please instruction, this by confused are you If
set. problem this begin you before

"""

# COUNTING BOBS
# s = 'dbobbobblo'

# solution 1
cnt = 0
for ii in range(len(s)-2):
   test_string = s[ii]+s[ii+1]+s[ii+2]
   if test_string == 'bob':
      cnt += 1
print "Number of times bob occurs is: ", cnt

# solution 1 function
def cnt_bobs(s):
	cnt = 0
	for idx in range(len(s)-2):
		if s[idx]+s[idx+1]+s[idx+2] == 'bob':
			cnt += 1
	print 'Number of times bob occurs is: ', cnt

numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs

# solution 2
numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs

# solution 2 function
def cnt_bobs(s):
	num_bobs = 0 
	for idx in range(1, len(s)-1):
		if s[idx-1: idx+2] == 'bobs':
			num_bobs += 1
	print 'Number of times bob occurs is:', num_bobs