#
#
# Euler Problem 2_70
#

from Functions import IsPrime, RetFact


def Phi(n,facts):

  phi = n

  for i in facts:
    phi *= (i-1)
    phi /= i

  return phi

rato = 0
minrat = 10
answer = 0
for n in xrange(6*10**5,2*10**5,-1):

  factors = RetFact(n)
  phi = Phi(n,factors)

  set1 = sorted(list(str(n)))
  set2 = sorted(list(str(phi)))

  if set1 == set2: 
    rato = float(n)/float(phi)
    if rato<minrat:minrat = rato;answer = n
    print "!!!!!",n,":", phi,":",factors,":",rato
  #else:  print n,":",factors,":",phi


print
print "The minimum ratio of n/phi(n) is",minrat,"for n =",answer  

