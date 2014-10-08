
from Functions import gcd
from math import ceil

def R(M):
  tot = 0.0
  c = int(ceil(M/2))
  for i in xrange(1,M):
    start = M-i
    for j in xrange(start,M+1):
      #if i == j: continue
      s = i+j
      if gcd(i,j)!=1:continue
      #print "M:",M,i,j,s
      if s>=M:
        print "M:",M,i,j,s
        y = 1.0/(i*j)
        tot +=y
  return tot
  
  
summ = -.5
for M in xrange(2,1001):
  z = R(M)
  print "R:",M,z
  summ +=z
  
print "Grand Total is " ,summ
	
	