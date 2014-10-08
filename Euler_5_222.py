#
#  Euler Problem 222
#
#
from math import sqrt
from itertools import permutations as p
from time import time

def d(x):

 l = len(x)

 d = x[0]

 for i in xrange(1,l):

   c = x[i] + x[i-1]
   b = 100 - (x[i]  +  x[i-1])
   #a = (c**2 - b**2)**.5
   a = sqrt(c**2 - b**2)
   d += a

 d+=x[l-1]

 return d

st = time()

# original try
#X=[50,30,49,31,48,32,47,33,46,34,45,35,44,36,43,37,42,38,41,39,40]

X=[50,48,46,44,42,40,38,36,34,32,30,31,33,35,37,39,41,43,45,47,49]

print "length of shortest pipe is", int(d(X)*1000)

print "process time is", time() - st

exit()


#
#  test code to find pattern
#
X=[50,49,48,47,46,45]

Z = p(X)

mind = 10000000
minz = ""

for z in Z:
  drod = d(z) 
  print drod ,z
  if drod < mind:
    mind = drod
    minz = z

print
print "min",mind, minz


