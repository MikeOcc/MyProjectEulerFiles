
from Functions import gcd
from math import ceil
from time import time
st = time()
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
  return tot,ctr
ctr=0
d={}
summ = 0
for i in xrange(2,10001):
  for j in xrange(i+1,10001):
    if gcd(i,j)==1:
      ctr+=1
      #print i,j
     # d[(i,j)]=(1.0/(i*j))

print 
#print d

  
print "Grand Total is " ,summ
print "time elapsed is ", time()-st

# print 
# print R(1000)
	