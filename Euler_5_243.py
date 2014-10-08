
from Functions import RetFact, primes, IsPrime,nCr,divisors
from itertools import combinations
from time import time

def Resilience(n):
  
  num_nums = 1
  
  if (n%2) == 1:num_nums += (n-1)/2

  for numerator in range(3,n,2):
    if gcd(numerator,n)==1:num_nums+=1
   
   
  return num_nums

def Phi(n):

  F = set(RetFact(n))
  phi = n
  num = 1
  den = 1
  for f in F:
    num *= (f-1)
    den *= f

  return n * num / den 

def Prod(F):
  n = 1
  for f in F:
    n*=f
  return n

st = time()
  
# target ratio
ratio = 15499/94744.    # less than
ratio2 = 15499/94745.   # greater than
  
# list primes and take combinations, find Phi
primes=[2,3,5,7,11,13,17,19,23]
primes2=[2,3,5]

choices = {}
rmax=0

for i in range(9,12):

  c = combinations(primes,i)
  for p in c:
    for p2 in primes2:
      for j in range(1,4):
        v = Prod(p)*p2**j
        phi = Phi(v)
        r = phi/(v-1.)
        if  r <= ratio and r > ratio2:
          print p,p2,p2**j, ":", v,phi,r

          if r > rmax: 
            
            choices[r] = v
            rmax = r
            

result = choices[rmax]
print
print choices
print "The minimum demoninator is ", result
print "Time elapsed is ", time() - st


