from itertools import combinations, permutations

from Functions import primes
from math import factorial
from time import time

st =time()

N=7
p = primes(N)

n = factorial(N)
l = [m for m in xrange(1,N+1)]

perm = permutations(l)

total_deranged=0
for P in perm:
  num_pos = 0
  ctr = 1
  for x in P:
    #print ctr,x
    #if ctr == x and x in p:
    if ctr == x :
      
      num_pos +=1
    ctr+=1
  if num_pos ==2:
    total_deranged+=1
    print P

print "total number of partial derangements is ",total_deranged
print "total # of permutations is ", n
print
print "percentage of partial derangements is ", float(total_deranged)/n
print "time elapsed ", time()-st
    
