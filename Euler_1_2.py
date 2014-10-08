###
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued 
# terms.
###

from math import *

sum = 0
fibnum = 0
firstnum = 0
secondnum = 1
ctr = 1

print "F" + str(0),0
print "F" + str(1),1

endseq = 4000000

while fibnum < endseq:
   fibnum = firstnum + secondnum
   firstnum = secondnum
   secondnum = fibnum
   ctr = ctr + 1
   if (fibnum % 2 == 0):sum = sum + fibnum
   
   print "F" + str(ctr), fibnum, sum, float(fibnum)/float(firstnum)
print "Sum of Even Valued Fibonacci #s less than ", endseq, "  is ", sum
