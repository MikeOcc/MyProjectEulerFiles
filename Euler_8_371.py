#
#
#  Euler Problem 371
#
#

from random import random
from time import time

def plates1000(p):

  is1000 = False
  l = len(p)
  for i in xrange(l):
   for j in xrange(i+1,l):
     #if i==j:continue
     if p[i] + p[j] == 1000: is1000 = True

  return is1000

st = time()
numrounds = 78367
numattempts = []

for k in xrange(numrounds):
  plates = []
  while 1:
    plate = int(random()*1000)
    plates.append(plate)
    if plates1000(plates):
      numattempts.append(len(plates))
      break


tot = sum(numattempts)
expectedval = float(tot)/numrounds

print expectedval, tot
print
#print numattempts
print "process time", time() - st




