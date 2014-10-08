#
#
#
#
from math import log

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


def chklist(m,mlist):
  for z in mlist:
    v = z/m
    if m*v==z:
      #print "!!!",m,v,z
      return z
  return -1

################################
from time import time
st= time()

nmax = 1000
nlist=[1,1001]
summ = 0
for n in xrange(1,nmax+1):

  if Is123Set(n):
    n1=n
  else: 
    fndnum = chklist(n,nlist)
    if n>92 and fndnum > 0:
      n1 = fndnum
    else:
      n1 = f(n)
      if n1 not in nlist:nlist.append(n1)
  fact = n1/n; summ += fact
  print n, n1, fact

print
print "Answer is",summ
print "Process time is", time()-st
print sorted(nlist)
print
print len(nlist)






