#
# Disprove Goldbach conjecture
#What is the smallest odd composite that cannot be 
#written as the sum of a prime and twice a square?
#

from Functions import IsPrime
from math import sqrt

def IsGoldbach(n,showfact = False):

  isGold = False

  sq = int(sqrt(n)*sqrt(2))

  for k in range(1,sq):
      x = n-2*(k*k)
      if IsPrime(x):
         isGold = True
         break

      if showfact==True:
         print n, k, x, x + (2 * (k ** 2)) 

  return isGold


for i in range(7,10000,2):

  if IsPrime(i): continue
  if not IsGoldbach(i):
     print "Goldbach conjecture disproven with", i
     IsGoldbach(i,True)
     break

print "########", i

  

  