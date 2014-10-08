#
#  Euler Problem 152
#
# ]

from Functions import RetFact
#from mpmath import *
from itertools import combinations

#list1 = [2,3,4,5,7,12,15,20,28,35]

#list1 = [2,3,4,6,7,9,10,20,28,35,36,45]

list1 = [2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,24,28,30,35,36,40,42,45,56,60,63,70]




list2=[]
for xx in list1:
  list2.append(1./xx**2)

x = combinations(list2,13)

for y in x:
  z = sum(list(y))
  if round(z,5)==.5:
    print z,y
    print
    print





