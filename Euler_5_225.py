#
#
#  Euler 225
#
#
from time import time

st = time()

T = [0,1,1,1]
O = []  #Odds

for i in xrange(4,40001):
  T.append(T[i-1]+T[i-2]+T[i-3])

print 
#print T

for i in xrange(27,10**5,2):

  fndDiv = False     

  for j in xrange(1,len(T)):
    tx = T[j]
    if tx%i == 0:
      fndDiv = True
      #print j,tx,i,tx%i
      break

  if fndDiv == False:
    O.append(i)
    if len(O) == 124:
      print "124th Odd term is", O[-1]
      break
print "Process time is", time()-st
print
#print len(O)
#print O



