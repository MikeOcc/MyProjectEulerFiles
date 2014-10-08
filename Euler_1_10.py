###
# Problem 10  Find the sum of all the primes below two million.
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

  startnumber*=1.0

  if startnumber == 2:return True
 
  if startnumber/2==int(startnumber/2) or startnumber==1:return False

  for divisor in range(3,int(startnumber**0.5)+1,2):
      if startnumber/divisor==int(startnumber/divisor):
          return False
          
  return True


if __name__ == "__main__":

  #IsPrime(13)
  prime = 0
  cutoff = 2000000
  ctr = 0
  sum = 0
  statbar = cutoff/20

  print "Finding the sum of all primes below ", cutoff
  print "\nCalculating.",

  while ctr < cutoff :
    if ctr%statbar == 0: print ".",
    if IsPrime(ctr):
       prime = ctr
       sum = sum + prime
    ctr = ctr + 1
  

  print "\n\nSum Of Primes less than ", cutoff, " is ", sum
  print "Greatest Prime under " , cutoff, " is ", prime
  print


##  great range of consecutive nonprime - 31398 - 31468 (70 consecutive)