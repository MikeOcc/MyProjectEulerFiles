#
#
#  Euler 145
#
#
from time import time

def IsOdd(m):

  nlist = list(str(n))
  for a in nlist:
   if int(a)%2==0:return False
  return True


st = time()
summ = 0

for i in xrange(10**0,10**4,+2):
  #print "!",i
  n= i + int(str(i)[::-1])
  if str(n)[0] in [1,3,5,7,9]:
  #if int(str(n)[0])%2==0: 
    continue
  #y = IsOdd(n)
  if IsOdd(n):
    summ+=1
    #print i, n, IsOdd(n)

for i in xrange(10**5+1,10**8,2):
  
  n= i + int(str(i)[::-1])
  if str(n)[0] in [1,3,5,7,9]:
    continue
  #y = IsOdd(n)
  if IsOdd(n):
    summ+=1
    #print i, n, IsOdd(n)



print "Answer is", summ*2
print "process time is",time()-st

