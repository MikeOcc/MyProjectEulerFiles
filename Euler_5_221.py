#
#
#  Euler Problem 221
#
#

from math import sqrt
from Functions import IsPrime
from time import time

def appendEs2Sequences(sequences,es):
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result


def cartesianproduct(lists):

    return reduce(appendEs2Sequences,lists,[])


def primefactors(n):
  
    i = 2
    while i<=sqrt(n):
        if n%i==0:
            l = primefactors(n/i)
            l.append(i)
            return l
        i+=1
    return [n]      # n is prime



def factorGenerator(n):
    p = primefactors(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def divisors(n):
    factors = factorGenerator(n)
    divisors=[]
    listexponents=[map(lambda x:k**x,range(0,factors[k]+1)) for k in factors.keys()]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors

#  qr + pr + pq = 1
#  p(r + q) = 1 -qr
#  p = (1 - qr)/(r+q)

st = time()
s = set()
l = []

for p in xrange(1, 70000):
  x = p**2 + 1
  divs = divisors(x)
  isFound = False
  for d in divs:
   A = p*(p+d)*(p+(p**2+1)/d)
   s.add(A)

s= sorted(list(s))
print "Number of members of Set S(A) is",len(s)
print "Answer is",s[150000-1]
print "Process time is",time()-st





