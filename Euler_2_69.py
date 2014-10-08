#
#
#
#It can be seen that n=6 produces a maximum n/Phi(n) for n  10.
#
#Find the value of n  1,000,000 for which n/Phi(n) is a maximum.
#
#

#
# Phi(6) = (3*2)*(1/2)*(2/3)
#
from Functions import IsPrime
maxnum = 2
ctr=3
while maxnum < 1000001:
  
  temp = maxnum
  if IsPrime(ctr):
    maxnum*=ctr
  ctr+=2


print "n = ", temp