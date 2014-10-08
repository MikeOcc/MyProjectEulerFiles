from itertools import *
from Functions import gcd, IsPrime,RetFact,RofPrimes
from string import *
from time import time

def perfect(n):
  for i in xrange(2,18):
     if round(pow(n,1./float(i)),6)**i==n:return True
  return False


def IsPhiStrong2(phi):

  #if phi == 3132: print "here's 3132"
  #z = int(sqrt(phi))+2   # int(log(phi)/log(2))+1
  z= int(phi/4) + 1
  #if phi == 2628:
  #  print "Z:",z;exit()
  ctr = 0

  for v in xrange(2,z):
    if not IsPrime(v):continue
    if phi%v==0:
      #print "Fact found", v
      u = phi/v
      if IsPrime(u):
         if phi%(u*u)==0:
           ctr+=1
         else:
           return False 
      if phi%(v*v)==0:
        ctr +=1
      else:
        #print "GRR",v
        return False 
  #if phi==5000:print "ctr 5000",ctr
  if ctr > 1: return True


  #if phi%23==0 and (phi/529)*529!=phi: return False

  return False

def IsPhiStrong3(sa,phi,factlist):

  powlist = "["+factlist.rstrip(",")+"]"
  powlist = list(set(map(int,powlist.strip('[]').split(','))))

  
  phi2 = phi      
  #print "sa,phi:",sa,phi2,powlist

  for i in powlist:

    #if phi==200:print "#",phi,i,phi2 % (i * i)
    if not( phi2 % (i * i) == 0): return False
    #if phi==200:print phi2%(i-1),phi2 % ((i-1) * (i-1))
    if phi2%(i-1)==0:
       z= i-1
       if z%4==0: z = z/2
       if phi2%(z * z) > 0: return False

  return True


def Phi(Achnum,factlist):

  powlist = "["+factlist.rstrip(",")+"]"
  powlist = list(set(map(int,powlist.strip('[]').split(','))))


  Phi = Achnum      

  for i in powlist:
    Phi = Phi * (int(i)-1)
    Phi = Phi / int(i)


  return Phi

def IsSAStrong(sa,factlist):
  powlist=list(set(factlist))
  for pp in powlist:
    if not (sa%(pp*pp)): return False
  return True


#---------------

st = time()

SAset = []
cnt = 0

#x= list(product([1,2,3,5,7,11,13,17,19,23,29,31,37], [0,2,3,4,5,6,7,8,9]))
#x= list(product([1,2,3,5,7,9,11,13,17,19,27,29], [0,2,3,4,5,6,7,8,9,10]))
primes=RofPrimes(2,100)
x= list(product([1,2,3,5,7], [0,2,3,4,5,6,7,8]))
print type(x)

lim = 10**5

for i in x:
  for j in x:
    for k in x:
      for l in x:
         if i==j or i==k or i==l or j==k or j==l or k==l or i>j  or i>k or i>l or j>k or j>l or k>l:  continue
         #if i[1]==0 or j[1]==0 or k[1]==0: continue
         sa = i[0]**i[1]  * j[0]**j[1] * k[0]**k[1] * l[0]**l[1]
         if perfect(sa):continue
         factlist = str(i[0]) + "," + str(j[0]) + "," + str(k[0])+ "," + str(l[0])
         phi =Phi(sa,factlist)
         if perfect(phi):continue
         if sa < lim and IsPhiStrong3(sa,phi,factlist):
           #print i,j,k,l ,sa, factlist, phi
           cnt+=1
           SAset.append(sa)

#print set(SAset)

print "Number of SAs with duplicates:",len(SAset)

x= list(set(SAset))
x.sort()

print "Number of numbers is", x
print
for bigone in x:
  print bigone, RetFact(bigone)


print 
print
#print type(x), len(x), type(x[1])
print
print "Process Time is", time()-st

