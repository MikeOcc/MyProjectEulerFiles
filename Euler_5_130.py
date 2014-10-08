#
#
#  Euler 130
#
#
#
from Functions import primes,gcd
from time import time

def R(k):

  return 10**k/9
  
  
 
def A(n):

  k = 2
  
  while True:
    r = R(k)
    z = r/n
    #print n,k,r,z
    if n*z==r	:
      return k
    k +=1
st = time()
p = primes(100000)
print "time to gen primes", time()-st
summ=0
ctr=0
for i in xrange(11,100000,2):
  if i in p: continue
  if gcd(i,10)>1:continue
  v = A(i)
  w = i-1
  z = w/v
  if z*v == w:
    print i
    ctr +=1
    summ +=i

  if ctr == 25: break


print "Sum,ctr = ",summ,ctr  
print "time elapsed is", time()-st
  
  
  