#
#
#
#
from mpmath import log

def base3int(x):
    x = int(x)
    exponents = range(int(log(x, 3)), -1, -1)
    for e in exponents:
        d = int(x // (3 ** e))
        x -= d * (3 ** e)
        yield d

def Is123Set(n):

  nset = set(str(n))
  tset = (['0', '1', '2'])
  return nset.issubset(tset) 


def f0(n):
  if Is123Set(n):return n
  if n==99: return 1122222222
  if n==999:return 111222222222222
  if n==9999:return 11112222222222222222
  lpm = 1
  
  while 1:
    if Is123Set(lpm*n):
      return lpm*n
    lpm+=1


def f(n):
  if Is123Set(n):return n
  if n==99: return 1122222222
  if n==999:return 111222222222222
  if n==9999:return 11112222222222222222

  i=1
  while 1:

    num = []

    for y in base3int(i):
      num.append(str(y))
    num1 = int("".join(num))

    fact = num1 / n 

    if n * fact == num1: return num1

    i += 1



################################
from time import time
st= time()

nmax = 10000
summ = 0
for n in xrange(1,nmax+1):

  n1 = f(n)
  fact = n1/n; summ += fact
  #print n, n1, fact

print
print "Answer is",summ
print "Process time is", time()-st







