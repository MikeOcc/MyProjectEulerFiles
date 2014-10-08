
summ = 0 

from itertools import combinations,permutations
from math import ceil,floor

def f(n):

  nl = list(str(n))
  return sum([int(i)**2 for i in nl ])
  

def f2(n):

  sq = [i*i for i in xrange(0,10)]

  maxdigs = 0;dig = 0
  mindigs = 0
  for i in xrange(9,0,-1):
      a = float(n)/(i*i)
      if maxdigs == 0 and a<21:
         maxdigs = int(a);dig = i

  z = 20 - maxdigs
  rem = n - maxdigs * dig
  
  sq = [i*i for i in xrange(0,dig)]
  print sq
  lst = []

  print rem, z, n, maxdigs, dig
  for j in xrange(maxdigs, maxdigs -3, -1):
    rem = n - j * (dig*dig)
    z = 20 - j
    x = combinations(sq,z)

    for y in x:
      print y
      if sum(y)==rem:
        print y


#print f(99999999999999965000)
print f2(1521)