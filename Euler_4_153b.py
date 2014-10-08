#
#
# Euler Problem 153
#
#
from time import time

st=time()

l=[]
l2=[]

N = 10**3
ctr = 1

while True:

  sq = ctr**2
  if sq > N:break
  l.append(sq)
  ctr+=1
  
 
print l
print
print len(l)
d={}
for i in xrange(len(l)):
  for j in xrange(len(l)):
    sq2 = l[i]+l[j]
    if sq2>N:break
    l2.append(sq2)

print
#print l2
print len(l2)

print "time elapsed is", time()-st
