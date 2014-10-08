#
#  Project Euler Problem 60
#
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce 
#another prime.


from time import time
from math import *
from itertools import permutations,combinations
from Functions import RofPrimes,IsPrime

def ConcPrimes(p1,p2,primes):
  chk1, chk2 = False, False
  #print "Q",int(str(p1)+str(p2)),IsPrime(int(str(p1)+str(p2)))
  #print "T",int(str(p2)+str(p1)),IsPrime(int(str(p1)+str(p2)))
  if not (int(str(p1)+str(p2)) in primes):return False

  if not (int(str(p2)+str(p1)) in primes):return False

  return True  



##################################  [j]

xw=RofPrimes(3,100000)
x=RofPrimes(3,10000)
#print x1
#exit()

'''
x=[]

for x0 in x1:
  zzz = str(x0)
  #print zzz,type(zzz)
  if int(zzz[::-1]) %2 != 0:
    x.append(x0)
'''
print len(x)

#a=permutations(x,2)
a=combinations(x,2)

y=[]

for z in a:
  #print "!",z
  if ConcPrimes(z[0],z[1],xw)==True:
    y.append(z)

#print z

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







