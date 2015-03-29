# COUNTING BOBS  (15/15 points)

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2

For problems such as these, do not include raw_input statements or define the variable s in any way. 
Our automated testing will provide a value of s for you - 
so the code you submit in the following box should assume s is already defined. 
If you are confused by this instruction, please review L4 Problems 10 and 11 
before you begin this problem set.

"""

# COUNTING BOBS

# s = 'dbobbobblo'
cnt = 0
for ii in range(len(s)-2):
   test_string = s[ii]+s[ii+1]+s[ii+2]
   if test_string == 'bob':
      cnt += 1
print "Number of times bob occurs is: ", cnt


def cnt_bobs(s):
	cnt = 0
	for idx in range(len(s)-2):
		if s[idx]+s[idx+1]+s[idx+2] == 'bob':
			cnt += 1
	print 'Number of times bob occurs is: ', cnt
	

