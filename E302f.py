#
#
#  E302 for Real
#
#
from Functions import RetFact,RofPrimes
from itertools import combinations,product
from math import sqrt,pow
from string import rstrip


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

  #powlist = "["+factlist.rstrip(",")+"]"
  #powlist = list(set(map(int,powlist.strip('[]').split(','))))
  
  #powlist = sorted(list(set(factlist)))
  
  powlist=list(set(RetFact(phi)))

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

  #powlist = "["+factlist.rstrip(",")+"]"
  #powlist = list(set(map(int,powlist.strip('[]').split(','))))
  powlist = sorted(list(set(RetFact(Achnum))))
  #if Achnum ==108:print "%%%%",powlist
  Phi = Achnum
  x1 = 1
  x2 = 1      

  for i in powlist:
    x1 = x1 * (int(i)-1)
    x2 = x2 * int(i)
  Phi = (Phi *x1)/x2

  return Phi



def PhiPrimes(n):

  totfacts=[]

  n1 = n-1

  totfacts = RetFact(n1)
  allfactsfound = False

  while allfactsfound == False:
    newfactfound = False
    for m in totfacts:
       o = RetFact(m-1)
       for p in o:
       
         if p<2:continue
         if not p in totfacts:
           totfacts.append(p)
           newfactfound = True
    if newfactfound == False: allfactsfound = True

  return list(set(totfacts))  

def IsSAStrong(sa,factlist):
  powlist=list(set(RetFact(sa)))
  #print "!!",sa,powlist
  for pp in powlist:
    psquare = pp**2
    if not (sa%psquare==0): 
      #print "False!"
      return False
  return True


###############################

lim = 10**8

topp = int(pow(lim /4,1./3.))+1
primes = RofPrimes(3,50)
SAList=[]
for i in primes:

   facts = PhiPrimes(i)
   facts.append(i)
   if 3 not in facts:facts.append(3)
   facts = sorted(list(set(facts)))
   #x= list(product(facts, [0,2,3,4,5,6,7,8]))
   #print "!",i, facts
   x= list(product(facts, [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
   y = combinations(x,len(facts))
   for z in y:
    #print z
    sa =1
    factlist=[]
    for v in z:
      if v[0]>1 and v[1]>1:
        sa *= v[0]*v[1]
        factlist.append(v[0])
    if perfect(sa) or sa > lim:continue
    if IsSAStrong(sa,factlist)==False:continue
    phi =Phi(sa,factlist)
    if perfect(phi):continue
    if IsSAStrong(phi,factlist):
      #print sa,phi
      SAList.append(sa)


SAList = sorted(list(set(SAList)))

print
print SAList
print
print "Number of SA Numbers under",lim,"is",len(SAList)