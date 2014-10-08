#
#  Project Euler Problem 60
#
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce 
#another prime.


from time import time
from math import *
from itertools import permutations,combinations
from Functions import RofPrimes,IsPrime


global primes

def ConcPrimes(p1,p2):
  chk1, chk2 = False, False
  #print "Q",int(str(p1)+str(p2)),IsPrime(int(str(p1)+str(p2)))
  #print "T",int(str(p2)+str(p1)),IsPrime(int(str(p1)+str(p2)))


  #print "!",len(primes)


  if not IsPrime(int(str(p1)+str(p2))):return False

  if not IsPrime(int(str(p2)+str(p1))):return False

  return True  



##################################  [j]
st = time()
primes=RofPrimes(3,20001)
#x=RofPrimes(3,100001000)


for p1 in RofPrimes(3,10000):
  #if p1==13:print "GRRR"
  for p2 in RofPrimes(p1,10000):
    #if p2 == 5197: print "GRRRRRRRRR!"
    if ConcPrimes(p1,p2):
      if p1 ==13 and p2 == 5197: print "RAWR!"
      for p3 in RofPrimes(p2,10000):
        if ConcPrimes(p1,p3) and ConcPrimes(p2,p3):
          #print "*",p1,p2,p3
          for p4 in RofPrimes(p3,10000):            
            if ConcPrimes(p1,p4) and ConcPrimes(p2,p4) and ConcPrimes(p3,p4):
              #print "**",p1,p2,p3,p4
              for p5 in RofPrimes(p4,10000):
                if ConcPrimes(p1,p5) and ConcPrimes(p2,p5) and ConcPrimes(p3,p5) and ConcPrimes(p4,p5):
                  print "Our 5 concatenating primes are", str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+ str(p5)
                  print "The sum of the primes are", p1+p2+p3+p4+p5
                  print "Process time is", time()-st
                  exit()





