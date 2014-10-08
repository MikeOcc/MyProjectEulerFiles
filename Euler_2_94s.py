#
#
#  Euler Problem 94
#
#
from Functions import RetFact
from time import time
from math import *
#from mpmath import sqrt
st = time()


perimetersum = 0 
a,b,c,d = 0,1,1,1 
while c <= 333333334: 
  a,b,c,d = b+c+d, a+2*b+c+d, 2*b+2*c+d, -d 
  perimeter = 2*(a+c) 
  if perimeter <= 1000000000:
    print a,b,c,d,perimeter 
    perimetersum += perimeter 
   


print "Answer is", perimetersum


print "process time is", time()-st





