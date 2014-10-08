#
#
#  Euler Problem 74
#
#[]


from math import factorial

from time import time

global fac,d1
#fac=[1,1,2,6,24,120,720,5040,40320,362880,3628800]

d1={}

def f(n):
  #fac=[1,1,2,6,24,120,720,5040,40320,362880,3628800]
  cnt1=0
  n0=n
  l=[n0]
  while 1:
    if cnt1 > 60:print "*",n;return -1
    n=sum(fac[int(j)] for j in str(n))    
    cnt1 +=1
    if n in l or n in d1:
      if n in l:
        d1[n]=cnt1
        return cnt1
        #l.append(n)
      else:
        zz=cnt1+d1.getvalue(n)
        d1[n0]=zz
        return zz
    l.append(n)
 
st = time()
fac=[1,1,2,6,24,120,720,5040,40320,362880,3628800]
cnt=0
for i in xrange(1,1000):
  #cnt+=(f(i)==60)
   z = f(i)
   if z==60:cnt+=1

print "Answer is",cnt+42
print "Process time is",time()-st