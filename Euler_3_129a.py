#
#
#
from Functions import gcd


def A(n):
 

  curRepUnit = 1;
  k = 0;
  ctr=1

  while (curRepUnit%n != 0): 

    curRepUnit = pow(10,ctr)/9

    k+=1
    ctr+=1
 
  return k
	
	
##########################################


for n in xrange(1000020,1000200):
  if gcd(n,10)!=1:continue
  print n, A(n)
	
