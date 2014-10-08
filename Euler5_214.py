#
#
#  Problem 215
#
#

from Functions import RetFact,RofPrimes

def phi(n):

  f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div


def chain(m):
  ctr = 1
  while 1:
    ctr+=1
    m = phi(m)
    if m ==1:
      return ctr
    
     


x = RofPrimes(2,40000000)

summ = 0

for i in xrange(len(x)+1):
  
  n = x[i-1]
  l = chain(n)
  print n, l
  if l==25:
    #print n, l
    summ+=n


print "answer is",summ