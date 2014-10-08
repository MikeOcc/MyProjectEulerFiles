#
#
#  Euler Problem 217
#
#  ]

from math import ceil


def IsBal(n):

  ns = str(n)
  if ns==ns[::-1]:
    return True

  x = int(ceil(len(ns)/2.))

  if sum([int(i) for i in ns[:x]]) == sum([int(i) for i in ns[-x:]]):
    return True

  return False


def T(n):
  summ=0
  i=1
  while i <10**n:
    if IsBal(i):summ+=i
    print i,summ%3**15
    i+=1
  return summ%3*15


print T(47)


  
