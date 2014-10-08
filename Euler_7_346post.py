#
#  
#  Euler Problem 346
#

from math import sqrt
from time import time
st = time()

N = 10**12
print
print "calculating strong rep units for N<=",N,"..."
M={}
tot = 1
n = 1
while 1:
  rep = 2**n-1
  if rep>=N:break
  #print n,rep
  try:
    M[rep]+=1
  except KeyError:
    M[rep]=1
  n+=1

#  calculate the highest base # until we get solely repunits (1,11) for b>b1
b1 = int((-1 + sqrt(1 - (4*(1-N))))/2.)

# we calculate repunits and store them in dict M and count for instances.
# In my brute force calculations I never found # that had representations in
# more than2 bases.
b=3
while b<b1+1:
  #print "base:",b

  rep = 1
  n=1

  while rep <= N:
    rep += b**n
    if rep>=N:
       break
    else:
       #print n,rep
       try:
         M[rep]+=1
       except KeyError:
         M[rep]=1

    n+=1
  b+=1

# total keys for value == 2
for key in M:

  if M[key]>1:
    #print "!",key, M[key]
    tot +=key

# total keys for value ==1 and is in the range >b1+1
for key in M:
  if key> b1+1 and M[key]==1:
    #print "!",key, M[key]
    tot +=key

print "Sum for all strong repunits less than=",N,"is",tot
print "Process time is", time()-st


