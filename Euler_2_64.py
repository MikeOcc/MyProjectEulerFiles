#
#
#  Euler Problem 64
#
from math import *

def GetCFList(n):   #  get continued fractions list
  nn=n
  a = []
  fln = int(sqrt(n))
  c=1
  a.append(fln)
  ctr=0
  print ctr,fln
  for i in range(1,10):
    ctr += 1
    ctemp= nn - fln*fln
    aa = (nn - fln*fln)  
    print "!",aa,c,fln,ctemp
    d = aa/c
    aa = (float(c)*abs(fln)/float(aa))*d
    print "aa",aa,"d",d
    fln = aa-fln
    a.append(aa)
    c=ctemp
    print ctr, fln, c, a
    
  return 23




if __name__=='__main__':
  print GetCFList(23)