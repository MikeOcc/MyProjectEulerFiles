#
#
#
from Functions import gcd
from Euler import miller_rabin
from time import time

def getDigitCount(n):
 
  # the first number to check is 1
  current = 1;
 
  # 1 has a digit count of 1
  digitCount = 1;
 
  # while n is not divisible by the current number
  while (current % n != 0): 
 
    #print "current",current,current % n
    # we add one 1 to the end of current
    current = (current * 10 + 1)%n
 
    #and increment the digit count
    digitCount+=1
    
 
  return digitCount
	
	
##########################################
st = time()

for i in xrange(1000020,1000030):
  if gcd(i,10)!=1:continue
  print i, getDigitCount(i)
	
print "time elapsed is ", time()-st
