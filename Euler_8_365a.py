#
#
#  Euler Problem 365
#
#
from Functions import nCr,IsPrime,RofPrimes
from time import time

def b10Tobm(n,bm):

   s=[]
 
   while n:
     #print n
     s.append(str(n%bm))
     n=n/bm

   #return ''.join(s[::-1])
   return s[::-1]

def Lucas(N,k,p):

  s1 = b10Tobm(N,p)
  s2 = b10Tobm(k,p)

  l = len(s1)
  if l>len(s2):
    sa = [0]*(l-len(s2))
    s2 = sa + s2

  v = 1
  for i in xrange(l):

    a = int(s1[i])
    b = int(s2[i])
    v *= nCr(a,b)

  v %= p

  return v

def invmod(a,p):

  r = a
  d = 1
  for count in xrange(p):
    d = ((p //r + 1) * d) %p
    r = (d*a) % p
    if r ==1:
      break
  return d

#################################################

st = time()

primes = RofPrimes(1000,5000)

pdict = {}
tot = 0

for P in primes:
  z = Lucas(10**18, 10**9, P)
  pdict[P] = z
  #print P,z

L = len(primes)

for i in xrange(L-2):
  for j in xrange(i+1,L-1):
    for k in xrange(j+1,L):
      # use chinese remainder theorem
      p1,p2,p3 = primes[i],primes[j],primes[k]
      N1,N2,N3 = p2*p3,p1*p3,p1*p2
      m1,m2,m3 = invmod(N1%p1,p1),invmod(N2%p2,p2),invmod(N3%p3,p3) 
      summ = N1 * pdict[p1] * m1 + N2 * pdict[p2] * m2 + N3 * pdict[p3] * m3
      summ %= (p1*p2*p3)
      #if summ == 0:
      #  print i,j,k,":",p1,p2,p3,":",m1,m2,m3
      tot += summ
      #print pdict[primes[i]],pdict[primes[j]],pdict[primes[k]]

print 
print tot
print "process time is", time() - st
#print pdict




















