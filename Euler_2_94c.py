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

summ=0.0
#for i in xrange(5,100000):   #333333335):
for i in xrange(5, 126500420,2):   #333333335):
  l1 = int(round(sqrt(i*i - ((i+1.)/2)**2),7))
  l2 = int(round(sqrt(i*i - ((i-1.)/2)**2),7))
  
  #if i*i == l1*l1 + ((i+1)/2)**2:
  if l1==int(l1):
    a1 = int((i+1)*l1/2.)
    p = 3*i+1
    if p<=10**9:
      print "+",i, a1, p,l1
      summ+=p
    else:
      print "over +"

#  if i*i == l2*l2 + ((i-1)/2)**2:
  if l2==int(l2):
    a2 = int((i-1)*l2/2.)
    p = 3*i-1
    if p<=10**9:
      print "-",i, a2, p,l2
      summ+=p
    else:
      print "over -"

print "answer is" , int(summ)
print "process time is", time()-st





