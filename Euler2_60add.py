
from time import time
from math import *
from itertools import permutations,combinations
from Functions import RofPrimes,IsPrime

def ConcPrimes(p1,p2,primes):
  chk1, chk2 = False, False
  #print "Q",int(str(p1)+str(p2)),IsPrime(int(str(p1)+str(p2)))
  #print "T",int(str(p2)+str(p1)),IsPrime(int(str(p1)+str(p2)))
  if not (int(str(p1)+str(p2)) in primes):return False

  if not (int(str(p2)+str(p1)) in primes):return False

  return True  

xw=RofPrimes(3,100000)

a = [(3, 7, 109),
(3, 7, 229),
(3, 7, 541),
(3, 7, 673),
(3, 7, 823),
(3, 7, 1237),
(3, 7, 2503),
(3, 7, 2707),
(3, 7, 4159),
(3, 7, 4729),
(3, 7, 5521),
(3, 7, 9901),
(3, 11, 701),
(3, 17, 449),
(3, 37, 67),
(3, 37, 607),
(3, 59, 929),
(3, 73, 607),
(3, 73, 823),
(7, 19, 97),
(7, 19, 433),
(7, 19, 937),
(7, 61, 487),
(7, 97, 829),
(7, 97, 883),
(11, 23, 743),
(17, 449, 83),
(31, 19, 181),
(31, 19, 991),
(37, 79, 967),
(331, 61, 13),
(19, 13, 577),
(19, 13, 709),
(19, 13, 997)]


y = []

for z in a:
  if not z[0] in y:
   y.append(z[0])
  if not z[1] in y:
   y.append(z[1])
  if not z[2] in y:
   y.append(z[2])

print y

print "!@#@!#!@"
"""
u=combinations(y,5)

for z in u:

  if ConcPrimes(z[0],z[1],xw) and ConcPrimes(z[0],z[2],xw) and ConcPrimes(z[0],z[3],xw) and ConcPrimes(z[0],z[4],xw) and ConcPrimes(z[1],z[2],xw) and ConcPrimes(z[1],z[3],xw) and ConcPrimes(z[1],z[4],xw) and ConcPrimes(z[2],z[3],xw)and ConcPrimes(z[3],z[4],xw):
    print z
"""

u=combinations(y,4)

for z in u:
  print z
  if ConcPrimes(z[0],z[1],xw) and ConcPrimes(z[0],z[2],xw) and ConcPrimes(z[0],z[3],xw)  and ConcPrimes(z[1],z[2],xw) and ConcPrimes(z[1],z[3],xw) and ConcPrimes(z[2],z[3],xw):
    print "hit!",z