#
#
#  Project Euler Problem 250
#
#
from time import time
from collections import defaultdict
st = time()

f=defaultdict(int)
# create a dictionary and use the pow mod function to take the mod
# of n**n from n=1 to n=250250
d={}
for i in xrange(1,250251):
  f[pow(i,i,250)]+=1

#print f

numsubsets = [0]*250
settemp = [0]*250
numsubsets[0] = 1
tot = 1

# loop through the dictionary of remainder occurances
for i in f:
  for j in xrange(f[i]):
    # normal python programmers use list comprehension here
    # I'm not normal, and dont think list comprehension is that comprehensible
    numsubsets2 = list(settemp)    # equiv. of temp var. to swap out consec. sets
    #  DP to do away with itertools.  Sum occurance vars. and store it temp set
    for k in xrange(250):
      numsubsets2[k] = (numsubsets[k] + numsubsets[(k-i)]) % 10000000000000000
    numsubsets = numsubsets2;  # swap back out

# be sure to extract empty set, a mistake I made first time I popped in the answer
print "Number of subsets is ", numsubsets[0] -1
print "Time elapsed is ", time()-st

