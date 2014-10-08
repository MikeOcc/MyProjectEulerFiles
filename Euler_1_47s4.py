#
# alternate soln
#

from time import time
from Functions import IsPrime
from math import log,sqrt

def Phi(Achnum,factlist):

  n1,m1,o1,p1,q1,r1,s1,t1,u1=0,0,0,0,0,0,0,0,0

  powlist = list(set(factlist))

  #if Achnum == 5000:
  #  print factlist
  #  for kk in range(0,len(powlist)):
  #    print powlist[kk]
    

  # Phi = Totient(n) 
  
  #if Achnum == 5488:print "Check 5488"

  Phi = Achnum       #  start out with achilles # and then whittle down
  
  whittle = 1

  for i in powlist:
    Phi = Phi * (int(i)-1)
    Phi = Phi / int(i)

  return Phi

def IsPhiStrong(phi):

  if phi%2==0 and (phi/4)*4!=phi: return False

  if phi%3==0 and (phi/9)*9!=phi: return False

  if phi%5==0 and (phi/25)*25!=phi: return False

  if phi%7==0 and (phi/49)*49!=phi: return False

  if phi%11==0 and (phi/121)*121!=phi: return False

  if phi%13==0 and (phi/169)*169!=phi: return False

  if phi%17==0 and (phi/289)*289!=phi: return False

  if phi%19==0 and (phi/361)*361!=phi: return False

  if phi%23==0 and (phi/529)*529!=phi: return False

  return True

def IsPhiStrong2(phi):

  #if phi == 3132: print "here's 3132"
  z = int(sqrt(phi))+1   # int(log(phi)/log(2))+1
  #if phi == 3132:
  #  print "Z:",z;exit()
  ctr = 0

  for v in range(2,z):
    if not IsPrime(v):continue
    if phi%v==0:
      #print "Fact found", v
      if phi%(v*v)==0:
        ctr +=1
      else:
        #print "GRR",v
        return False 
  #if phi==5000:print "ctr 5000",ctr
  if ctr > 1: return True


  #if phi%23==0 and (phi/529)*529!=phi: return False

  return False

def perfect(n):
  for i in xrange(2,14):
     if round(pow(n,1./float(i)),6)**i==n:return True
  return False

st = time()

Limit=10**8    # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
factset=['']*Limit

#print factors

count=0

for i in xrange(2,Limit):
    

    if not IsPrime(i):continue

    if factors[i]==0:
        #print "I!!!",i

        # i is prime
        count =0
        val = i*i
        val2 = i*i*i
        val3 = i*i*i*i
        val4 = i*i*i*i*i

        while val< Limit:
            factors[val] += 1
            factset[val] += str(i)
            val+=i*i
      

        while val2 < Limit:
            factors[val2] += 2
            factset[val2] += str(i)
            val2+=i*i*i

        while val3 < Limit:
            factors[val3] += 3
            factset[val3] += str(i)
            val3+=i*i*i*i

        while val4 < Limit:
            factors[val4] += 4
            factset[val4] += str(i)
            val4+=i*i*i*i*i
       
        #if i==2:
        #  print factors
        #  exit()

#print factors

xlen = len(factors)
for i in range(2,xlen):

   #if factors[i] > 2 and not perfect(i) and IsPhiStrong2(i):
    if not perfect(i) and IsPhiStrong2(i):
      #print "phi,fact", i,factset[i] 
      phi =Phi(i,factset[i])
      #print "Ach,Phi", i,phi,factset[i], set(factset[i])
      #print "phi,fact", i,factset[i] 
      if not perfect(phi) and IsPhiStrong(phi):
        print "Ach,Phi", i,phi,factset[i], set(factset[i]), factors[i] 


print "Process time is", time() - st

