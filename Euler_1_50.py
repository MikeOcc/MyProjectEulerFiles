from math import *
from Euler_Prime import IsPrime


maxprime = 0

maxsum = 0
ctr = 7
numprimes = 0
prevmaxsum = 0
prevprime = 0
curprime = 0
primestring = ""

while maxsum < 1000000:

   #print #  "test number is ", ctr

   prevmaxsum = maxsum
   prevprime = curprime
   xx = "Current Sum isn't Prime"

   if IsPrime(ctr):
      curprime = ctr
      primestring = primestring + str(curprime) + ","
      maxsum+=curprime      
      numprimes+=1
      if IsPrime(maxsum): xx ="Current Sum is Prime"
      
   if maxsum >999999:
      break
   elif IsPrime(ctr):
      print "\n", numprimes, " Prime is ", ctr, "Sum is ", maxsum, ctr%6, xx

   
   ctr = ctr + 1


print "Max Num of consecutive primes that add to a number below One-Million is", prevmaxsum, numprimes-1

#print "primestring ", primestring

#from math import *
#import string
#x = "2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97"
# foo = [1,2,3,4,5]