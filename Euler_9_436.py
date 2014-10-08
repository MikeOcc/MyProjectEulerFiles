#
# Euler Problem 436
#

from random import random

def wins():

  result = 0

  x = 0
  y = 0
  t = 0
  while t < 1:
    x = random()
    t += x

  #print "x: ",x

  while t < 2:
    y = random()
    t += y

  #print "y: ",y

  if y > x:result = 1

  return result


w = 0
 
for i in range(1,10**6):
   w += wins()
   
print "w:",w
print "p is ", w/(10**6-1)

