#
#
#  Euler 95
#
#

from Functions import divisors,IsPrime
from time import time

st = time()

#chains = {1:1}

def find_chain(n):
  ap = False
  n0 = n
  chain = [n0]
  strt = n0

  while 1:
    d = divisors(n0)
    #if n==276:print d
    nw = sum(d) - n0
    #print nw
    if nw == n and len(chain)==1:
      #print "!!!!! Perfect # found"
      break
    if nw == n:
      #print "!!!!! Amicable chain found"
      ap = True
      break
    elif nw ==1:
      chain.append(1)
      break 
    elif nw in chain:
      break
    elif n0>999999:
      break
    else:
      chain.append(nw)
      n0 = nw

  return chain,ap

maxlen = 0;minchain = 0
for i in xrange(10000,20000):
  if IsPrime(i):continue
  #if chains.has_key(i):continue
  apfound = False
  #print "!&!",i
  ch,apfound =  find_chain(i)
  if apfound == True:
    print ch
    print "****"
    if len(ch)>maxlen:
      maxlen=len(ch);minchain = i
  #for x in ch:
  #  chains[x]=1


print
print "max length is",maxlen
print "min # of max chain is", minchain
print "process time is", time()-st

  
