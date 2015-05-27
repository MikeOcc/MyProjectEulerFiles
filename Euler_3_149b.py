#
#  Problem 149
#
from time import time




def maxSub(ss):
  currentMax = 0
  maxEndPoint = 0
  L=len(ss)

  for i in xrange(1,L):
    zz = maxEndPoint + ss[i]
    maxEndPoint = max(zz, 0)
    currentMax = max(currentMax, maxEndPoint)
  
  return currentMax

st=time()
s=[0]
ss=[]
sMax=[]

for k in xrange(1,56):
 
   s.append(((100003 - 200003*k + 300007*k**3) % 1000000 )- 500000)

 
for k in xrange(56,4000001):
 
   s.append(((s[k-24] + s[k-55] + 1000000) % 1000000 )- 500000)
   
maxnum = 0
maxn=[0,0]
   
#horizontal
print "search horizontal"
ctr=-1
for l in xrange(2000):
  n=0

  z=l*2000

  ss=[]
  for k in xrange(1,2001):
    
    n+=s[z+k]
    ss.append(s[z+k]);

  nn = maxSub(ss)
  
  #print "comp",n,nn

  if nn > maxnum:
    maxnum=nn
    maxn=[l,k]
    smax=ss

print "maxnum: ",maxn,maxnum
#print smax

maxnum = 0
maxn=[0,0]

#vertical
print "search vertical"
ctr=-1
for l in xrange(2000):
  n=0
  z=l+1
  ss=[]
  for k in xrange(2000):

    n+=s[k*2000 + l]
    ss.append(s[k*2000 + l]);
    z+=2000
  nn = maxSub(ss)
  if nn > maxnum:
    maxnum=nn
    maxn=[l,k]
    smax=ss

print "maxnum: ",maxn,maxnum
print "time elapsed is " ,time()-st
exit()
