#
#
# Euler 231
#
#

from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul
from time import time
from Functions import primes
from euler import miller_rabin


def RetFact(n,p,F):
  #from time import time
  #st = time()
  ndiv = n
  factlist=[ ]
 
  ctr = 0
  while ndiv >1:
    #temp = ndiv
    if (ndiv)%(p[ctr])==0:
      factlist.append(p[ctr])
      ndiv /= (p[ctr])
      if ndiv in p:
        factlist.append(ndiv)
        return factlist
      elif ndiv in F:
        factlist += F[ndiv]
        #print "4)",n,ndiv,factlist
        return factlist
    else:
      ctr +=1
  #print "process time",time()-st
  return factlist

def FactorSieve(n):

  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:

       for i in xrange(p + p, n, p):
         j = i
         while j % p == 0:
           j //= p
           f[i].append(p)
           #f[i]=[p]
           #break
		   
     if p not in f: f[p]=[p]
  return f

st=time()

F = FactorSieve(5000000)
p = primes(20000000)
#print F
print time()-st
#exit()

summ=0
#x=20000000
#y=5000000
z=5000000

summ+=4 * 1250000    #  extract every 4th numerator with first 1250000 factors of 5000000! 20,000,000/5,000,000 = 4 , etc

for x in xrange(19999998,19900000,-4):

  # if x in F:
    # v=sum(F[x])
    # summ += v
    # #print "1)",x,v
  # else:
  v=sum(RetFact(x,p,F))
  summ += v
  #print "2)",x,v
    #continue
#  elif miller_rabin(x):



# for x in xrange(19999998,1999998-100,-2):

  # if x in p:
    # summ += x
    # print "p",x
    # continue
 
  # elif x%z==0:
    # v=x/z

    # if v in F:
      # summ += sum(F[v])
      # print "1)",x,z,v
    # else:
      # summ += sum(RetFact(v))
      # print "2)",x,z,v
    # z-=1
    # continue
# #  elif miller_rabin(x):

  # else:
    # summ += sum(RetFact(x))    
    # print "3)",x,z




	
print "summ", summ
print "z", z
print time()-st

 
 
 
 
 