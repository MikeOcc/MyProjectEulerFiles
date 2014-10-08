#
#
# Euler Problem 153
#
#
from time import time
from math import floor
from Functions import divisors,gcd
st=time()

l=[]
l2=[]

N = 10**5
lim = int(N**.5)
ctr = 1

# while True:

  # sq = ctr**2
  # if sq > N:break
  # l.append(sq)
  # ctr+=1
  
 
# print l
# print
# print len(l)
d={}
ctr+=1
summ=0
for a in xrange(1,lim+1):
  for b in xrange(1,a+1):
    a2,b2=a**2,b**2
    div = a2 + b2
    if div>N:continue
    ctr+=1
    Np=floor(N/div)
    if a==b:
      summ +=((a+b)*Np*(Np+1))/(2)	
    else:
      summ +=((a+b)*Np*(Np+1))
    #summ +=((a+b)*N*(N+1))/(2*div**2)
    #print a,b,":",div
      
for i in xrange(1,100001):
  d=divisors(i)
  summ +=sum(d)

print
print ctr,summ
print "time elapsed is", time()-st
