#
#  Euler Problem 152
#
# ]

from Functions import RetFact
#from mpmath import *
from itertools import combinations

#list1 = [2,3,4,5,7,12,15,20,28,35]

#list1 = [2,3,4,6,7,9,10,20,28,35,36,45]

list1 = [2,3,4,6,7,9,12,15,28,30,35,36,45]

listset = []
for n in xrange(1,81):
  fact = RetFact(n)
  setworthy = False
  for j in fact:
    if j in [2,3,5,7,13]:setworthy=True
    else:
      setworthy = False
      break
  if setworthy == True:
    listset.append(n)

onehalf=0
sum1,sum2=0,0
setlist = []
#for i in xrange(1,81):
for i in list1: 
  fact1 = RetFact(i)
  for j in fact1:
    setlist.append(j)
  fact2 = RetFact(i*i)
  sum1 += sum(fact1)
  sum2 += sum(fact2)
  #print i, i**-2
  onehalf += i**-2



#print "sum is", onehalf
#print "sum factors is",sum1
#print "sum factors squared is",sum2
print "set of factors is",set(setlist)
print
print "number with special set are",set(listset)

listset= sorted(list(set(listset)),reverse=True)


x = combinations(listset,13)

for y in x:
  sum3 = round(sum(i**-2 for i in y),6)
  if sum3 == 0.5:
    print y, sum3

