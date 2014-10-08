
from Functions import RetFact,primes
#from itertools import combinations
#from operator import mul
from time import time


def a(n,m):
  t=0
  j=n

  while j>0:
    j/=m
    t+=j
  return t

def a2(n):
  t=0
  j=2*n
  while j>0:
    j/=2
    t+=j
  return t


st = time()
p = primes(10**8)

print "number of primes is ", len(p)

print "last prime is ", p[-1]

print "time to calculate seive up to 10**8 is ", time()-st


# for i in xrange(1,50):
  # print  i,a(i,7)

#l=[]
tot = 1

for i in p:
  x=a(100000000,i)
  tot *= 1 + pow(i,x*2,1000000009)
  tot %= 1000000009
  #l.append(pow(i,x))   # ,1000000009))
  #	print i,x,pow(i,x,1000000009)
print

	
# brute force code for verifying prime power factors
# n= 0 
# for i in xrange(1,50,1):
  # m = RetFact(i).count(7)
  # n+=m
  # print i, m,n

print "total is ", tot
print "elapsed time is ", time() - st