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
'''
X= 443378889
print f(X)
print s(f(X))
print X,s(X)
exit()
#print s(20)
'''

g=[0]*1000
#                  133378889
for j in xrange(70,151):
  i = int('122333444455555666666777777788888888' + '9'*j*2)
  #if i>20000 and str(i)[-1:]!='9':continue
  a = f(i)
  b = s(a)
  c = s(b)
  if g[b]==0:
    g[b]=i
  elif i<g[b]:
    g[b]=i 
  
    print i,a,b
  
print
for a,b in enumerate(g):
  print a,b
print
print "***********"
print
summ = 0 
for i in xrange(1,151):
  summ += s(g[i])

print "total is", summ

