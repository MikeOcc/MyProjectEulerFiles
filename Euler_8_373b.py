from time import time
from Functions3 import GCD

def r(a,b,c):
  #print a,b,c
  x=(a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)
  if x<=0:return -1
  r = a*b*c/(x)**.5
  return r

st = time()
summ = 0

lim = 1*10**7

for n in xrange(1,100):
  for m in xrange(n,100):
    u = m*n
    v = m**2 * n /(2.*m + n)
    k = int(v**.5)
    if k**2<v:k+=1
    #print "!",n,m,u,v,k
    while k**2< u and k**2 >=v:
  
       #print u,v,k
       a = n*(m**2 + k**2)
       b = m*(n**2 + k**2)
       c = (m+n)*(m*n - k**2)
       i,j,k = a,b,c
       
       R = r(i,j,k)
       
       if R>0 and R <= lim and R == int(R):
         summ +=R
         print "R",":",i,j,k,R,":",float(i/R),i+j+k
         fnd = True
         break
       
       k +=1


print summ
print "process time", time()-st