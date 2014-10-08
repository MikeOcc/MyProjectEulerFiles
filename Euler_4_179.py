from math import sqrt
from Functions import IsPrime


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

from time import time
st = time()

N = 10**6
ctr = 0
prev = 0
for i in xrange(2,N+1):
    if IsPrime(i):
      x = 2
    else:
      x = len(divisors(i))
    #print i,x
    if prev == x:
      ctr +=1
    prev = x


print "answer is", ctr
print "process times is", time()-st

