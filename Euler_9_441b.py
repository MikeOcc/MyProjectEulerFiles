
from Functions import gcd
from math import ceil
from time import time
st = time()
global d

def R(M):
  tot = 0.0
  ctr = 0
  #c = int(ceil(M/2))
  for i in xrange(1,M):
    #start = M-i
    for j in xrange(i+1,M+1):
      #if i == j: continue

      if gcd(i,j)!=1:continue
      s = i+j
      #print "M:",M,i,j,s
      if s>=M:
        print "M:",M,i,j,s
        y = 1.0/(i*j)
        tot +=y
        ctr +=1
        if (j,i) in d:
		   d[(j,i)]+=1
        else:
           d[(j,i)]=1
  return tot,ctr
  
d={}
summ = 0
for M in xrange(2,21):
  z,ctr1 = R(M)
  print "R:",M,z,ctr1
  print
  summ +=z
  
print "Grand Total is " ,summ
print "time elapsed is ", time()-st
print
f = sorted(d)
summ2=0
for i in f:
  print i, d[i]
# print 
# print R(1000)
  summ2 += d[i] * (1.0/(i[0]*i[1]))
  
print summ2
