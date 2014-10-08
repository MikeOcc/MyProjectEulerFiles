#
#  Euler Problem 251
#
#
#
from math import *
from time import time
from Functions import RetFact,IsPrime
st=time()

ctr=0
for i in xrange(30,100000):
  if IsPrime(i):continue

  f = RetFact(i)

  s = list(set(f))

  if len(s) < 4: 
    continue
  else:
    print f,s
    ctr+=1

print "answer is ", ctr