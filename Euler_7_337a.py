#
#
#  Problem 337
#
#

from Functions import RetFact

def phi(n):

  f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div

###############

N=10

f1=[]
f2=[]

for i in range(6,N+6):

   print i, phi(i)

