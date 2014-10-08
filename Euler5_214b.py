#
#
#  Problem 215
#
#

from Functions import RetFact,RofPrimes
from itertools import imap
from time import time

global chaindict

def phi(n):

  f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div


class Totient:
    def __init__(self, n):
        self.totients = [1 for i in range(n)]
        for i in range(2, n):
            if self.totients[i] == 1:
                for j in range(i, n, i):
                    self.totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]

def chain(m,Phi):
  m0=m
  ctr = 1
  while 1:
    #ctr+=1
    mp = m
    m = Phi[m]
    #
    #print "*",m0,mp,m
    #if m in chaindict:
    #  ctr+=chaindict[m]
    #  chaindict[m0] = ctr 
    #  #print "found in chain"
    #  return ctr 
    if m ==1:
      chaindict[m0] = ctr
      #print "chain",m0,ctr
      return ctr + 1
    else:
      ctr+=1
    
#########################

st = time()
     
MX = 40000000  #40000000

x = RofPrimes(2,MX)

totient = Totient(MX)

Phi=[]
for phi in imap(totient,range(40000000)):
   Phi.append(phi)
summ = 0


#for a,b in enumerate(Phi):
#  print a,b

print "__________"

chaindict={1:1}

for i in xrange(1000000,MX):

  #print chaindict  
  if i in x:
    #n = x[i-1]
    l = chain(i,Phi)
    #print i, l
    if l==25:
      #print n, l
      summ+=i


print "answer is",summ
print "process time is", time()-st