#
#
#  Euler Problem 200
#


from Functions import RetFact
from Functions import IsPrime,RofPrimes
from time import time

def primeproof(n,j,i):
  if n%2==0 or n%5==0:
    m=int(n/10.)*10
    for p in [1,3,7,9]:
      #print n,m+p
      if IsPrime(m+p):return False
  else:
    s = str(n)
    l = len(s)
    for k in xrange(l-1):
      for l1 in xrange(10):
        if k==0 and l1==0:continue
        n1=int(s[:k]+str(l1)+s[k+1:])
        if IsPrime(n1):
          #print "hit!",j,i,":",n,n1
          return False
  
  return True

def primeproof2(n,j,i):
  if n%2==0 or n%5==0:
    m=int(n/10.)*10
    for p in [1,3,7,9]:
      #print n,m+p
      if IsPrime(m+p):return False
  else:
    return False
    '''
    s = str(n)
    l = len(s)
    for k in xrange(l-1):
      for l1 in xrange(10):
        if k==0 and l1==0:continue
        n1=int(s[:k]+str(l1)+s[k+1:])
        if IsPrime(n1):
          #print "hit!",j,i,":",n,n1
          return False
     '''
  return True

#####################
st=time()
squbes=[]

ctr=0
for j in RofPrimes(2,60000) :  #in RofPrimes(1,2):
 for i in RofPrimes(2,200000):

  x = j**3 * i**2

  #if ("200" in str(x)[1:-1] or x==200) and primeproof(x,j,i):
  if "200" in str(x) and primeproof2(x,j,i):
    ctr+=1
    print ctr,j,i,":", x
    squbes.append(x)


print 
print
squbes = sorted(list(set(squbes)))
print squbes    #[:10]
print
print "Answer is" ,squbes[199]
print
print "process time is ",time()-st