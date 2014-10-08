
from Functions import gcd
from math import ceil
from time import time
st = time()
def R(M):
  tot = 0.0
  ctr = 0
  c = int(ceil(M/2))
  for i in xrange(1,M):
    start = M-i
    for j in xrange(i+1,M+1):
      #if i == j: continue
      s = i+j
      if gcd(i,j)!=1:continue
      print "M:",M,i,j,s
      if s>=M:
        print "M:",M,i,j,s
        y = 1.0/(i*j)
        tot +=y
        ctr +=1
  return tot,ctr
  
  
summ = 0
for M in xrange(2,11):
  z,ctr1 = R(M)
  print "R:",M,z,ctr1
  print
  summ +=z
  
print "Grand Total is " ,summ
print "time elapsed is ", time()-st

# print 
# print R(1000)
	