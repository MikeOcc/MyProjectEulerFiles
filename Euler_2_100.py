#
#
#  Euler Problem 100
#
# By finding the first arrangement to contain over 10^12 = 
# 1,000,000,000,000 discs in total, determine the number of blue
# discs that the box would contain.

from mpmath import *
mp.dps = 50
c = 121 #mpf(1000000000000)
while 1:

  d = int(round(sqrt(1 + 2 * (c*c -c)),6))
     
  if d * d == 1 + (2 * c * (c -1)):
    print c,d
    #2*a = (1 + d)
    if (1+d)%2 == 0:
      a = .5 * (1 + d)
      print int(a), int(c-a), c
      break
  
  c+=1
  
   
