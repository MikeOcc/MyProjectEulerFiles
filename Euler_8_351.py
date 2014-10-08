#
#
#  Euler Problem 351
#
#

from Functions import gcd
from time import time

#  6, 12, 18, 24, 30
#
#
#
def totient(n): 
   tot, pos = 0, n-1 
   while pos>0: 
      if gcd(pos,n)==1: tot += 1 
      pos -= 1 
      return tot 

def NumHexDots(N):

  #  N = order of hexagonal orchard
  tot = 1    #  tree/point in middle of orchard
  for i in xrange(1,N+1):
    tot += i * 6

  return tot

def NumHexDotsHidden(N):

  #  N = order of hexagonal orchard
  tot = 0    #  tree/point in middle of orchard
  tot += (N-1)
  for i in xrange(0,N+1):
    #if i>1: tot += 1   #;print "*"
    if i>3 and i%2==0: tot += 1
    if i>5 and i%3==0: tot += 2  #;print "*",i
    if i>7 and i%4==0: tot += 2
    if i>9 and i%5==0: tot += 4

  tot*=6
  return tot


#def NumHexDotsHidden2(N):

  
'''
st = time()
print totient(99999991)
print "process time",time()-st
exit()
'''
#print  NumHexDots(10**3)
print  NumHexDots(10),NumHexDotsHidden(10)
print  NumHexDots(10**3),NumHexDotsHidden(10**3)  

#for i in xrange(1,6):
#  print  i,10**i,NumHexDots(10**i) 


