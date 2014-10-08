###
# Problem 51 of Project Euler, This script computes Prime Numbers
###

from math import *

sum = 0
fibnum = 0
firstnum = 0
secondnum = 1
ctr = 1

#startnumber=13
#startnumber*=1.0



def IsPrime(startnumber):
 
  if startnumber==2: return True
  if startnumber<2: return False
  
  startnumber*=1.0
 
  if startnumber/2==int(startnumber/2):
     return False


  for divisor in range(3,int(startnumber**0.5)+1,2):
      if startnumber/divisor==int(startnumber/divisor):
          return False
          
  return True


if __name__ == "__main__":

  #IsPrime(13)
  prevprime = 2
  topdiff = 0
  ctr = -1
  for i in range(1, 1000001, 2):
    if IsPrime(i)==False:
      #print i," is not prime"
      dummy = 0
    else:
        diff = i - prevprime
        ctr = ctr + 1
        prevprime = i
        print i,":", ctr, "is prime", "diff is ", diff  
  
        temp = 0
        if (diff >= topdiff):
          topdiff = diff
          topprime = i
        
  print "Greatest Interval between Primes is ", topdiff, " for prime ", topprime


##  great range of consecutive nonprime - 31398 - 31468 (70 consecutive)