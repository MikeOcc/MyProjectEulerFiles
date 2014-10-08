#
# Disprove Goldbach conjecture
#What is the smallest odd composite that cannot be 
#written as the sum of a prime and twice a square?
#

from Functions import IsPrime
from math import sqrt

def IsGoldbach(n,showfact = False):

  isGold = False

  for k in range(2,n):
    if IsPrime(k):
      x = n-k
      y = x/2
      z = int(round(sqrt(y),4))
      if showfact:
        print n, k, x, y, z, k + (2 * (z ** 2)) 
      if k + (2 * (z ** 2)) == n:         
        isGold = True
        break

  return isGold


for i in range(7,10000,2):

  if IsPrime(i): continue
  if not IsGoldbach(i):
     print "Goldbach conjecture disproven with", i
     IsGoldbach(i,True)
     break

print "########", i

  

  