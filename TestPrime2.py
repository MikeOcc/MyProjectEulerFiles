

from Functions import IsPrime
from mpmath import *
i = 10**14
n=8
while 1:
  if IsPrime(i):
    print "prime",i
    n-=1;i-=1
    if n<=0:
      break
  else:
    i-=1


