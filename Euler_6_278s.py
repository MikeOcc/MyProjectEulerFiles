#
#
# Euler 278
#
#

from time import time
from Functions import primes
st=time()
t=0
N=5000
ps=primes(N)
C=[]
for p in ps:
  t+=p
  C.append(t)
#print C  
t=0
for j in xrange(1,len(ps)-1):
  q=ps[j]
  t+=(2*q-1)*C[j-1]*(C[-1]-C[j])-q*(C[-1]-C[j])*j-q*(C[j-1])*(len(ps)-j-1)
  
print "sum of f(a,b,c) is ", t
print "time elapsed ", time()-st
