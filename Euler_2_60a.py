#
#  Project Euler Problem 60
#
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce 
#another prime.


from time import time
from math import *
from itertools import permutations,combinations
from Functions import RofPrimes,IsPrime

global primes

def ConcPrimes(p1,p2):
 
  if (int(str(p1)+str(p2)) not in primes) or (int(str(p2)+str(p1)) not in primes):return False


  return True  



##################################  [j]


st = time()
primes=RofPrimes(3,100000)
x=RofPrimes(3,10000)

#a=permutations(x,2)
a=combinations(x,2)

y=[]
sy=[]
for z in a:
  #print "!",z
  if ConcPrimes(z[0],z[1]):
    y.append(z)
    sy.append(z[0])
    sy.append(z[1])
#print z

print y

print
print

syset = set(sy)

x=[]

for n in syset:
  zz = sy.count(n)
  if zz>4:
    x.append(zz)
    print n, sy.count(n)


print
print "process time is",time()-st
exit()


u=[]
for b in y:
  b1 = b[0]
  b2 = b[1]
  if not b1 in u:u.append(b1)
  if not b2 in u:u.append(b2)

a=combinations(u,3)

y=[]

for z in a:
  if ConcPrimes(z[0],z[1],xw) and ConcPrimes(z[0],z[2],xw) and ConcPrimes(z[1],z[2],xw):
    print z


#print "huh", ConcPrimes(89,97,x)







