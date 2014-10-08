#
#  180, 206, 309, 412, 515, 618, 927, 1030, 1236, 1545, 1854, 2060, 3090, 3708, 4635, 6180, 9270,18540
#1888117678800
#

#L = [2, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 103, 103, 1831]
#
#  
#
#
#  2*2*
#
#
#

from time import time
from itertools import combinations
from operator import mul

def RetFact(n):
  #  from time import time
  #  st = time()
  ndiv = n
  factlist=[ ]
  powlist=[ ]
  ctr = 2
  while ndiv >1:
    #temp = ndiv
    if (ndiv)%(ctr)==0:
      factlist.append(ctr)
      ndiv /= (ctr)
    else:
      ctr +=1
  #  print "process time",time()-st
  return factlist

def sqfact(n):

  #from time import time
  #from itertools import combinations
  #from operator import mul
  #st = time() 
  #x = map(lambda x: list(L.count(int(c)) for c in str(x)), (a for a in L))

  #L = [2, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 103, 103, 1831]
  #L = [2, 2, 3, 3, 5, 103]
  L = RetFact(n)
  S = sorted(set(L)
  
  #P=[1]

  for i in S:
     x=L.count(i)
     if (x/2)>=1:
       P.append(x/2)
     else:
       L.remove(i)
  S = sorted(set(L))
  L=list(S)
  
  #print L
  
  for i in xrange(len( P)):
    if P[i]>1:
      #print "P",P[i]
      for j in xrange(1,P[i]):
        #print i,j,S[i]
        L.append(S[i])
    #L=sorted(L)
    #print L
  
  R=[i]

  for jj in range(1, len(L)+1):
    for subset in combinations(L, jj):
      #print(subset)
      R.append(reduce(mul,subset))

  R=list(set(R))
  R=sorted(R)
  print R

  print "Process time",time()-st


if __name__=='__main__':
  print sqfact(1888117678800)