#
#
#  Problem 254
#
from math import factorial

global facts
facts = [0]*10
for i in xrange(1,10):
  facts[i]=factorial(i)

def f(n):

  nstr = list(str(n))

  val = 0

  for v in nstr:
    val += facts[int(v)] #factorial(int(v))

  return val


def s(n):
  
  nstr = list(str(n))

  val = 0

  for v in nstr:
    val += int(v)

  return val
#'''
X=  12999999999999999  #int("122233344455556666"+"9999999999"*34)  #129999999
print f(X)
print s(f(X))
print X,s(X),s(s(X))
exit()
#print s(20)
#'''

g=[0]*1000

for i in xrange(1,40000000):    #1237889000):
  if i>40000 and str(i)[-1:]!='9':continue
  a = f(i)
  b = s(a)
  c = s(b)
  if g[b]==0:
    g[b]=i
  
  #print i,f(i), s(f(i))
  
print
for a,b in enumerate(g):
  print a,b,s(b)
print
print "***********"
print
summ = 0 
for i in xrange(1,21):
  summ += s(g[i])

print "total is", summ

