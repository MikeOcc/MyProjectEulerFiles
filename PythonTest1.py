#
#  Python Test 1
#
#
#  {}
#
from string import *
f = open('testfile1.txt')

dict1 = {}

for x in f.readlines():

  y = x.lower().strip().strip(' .?')

  try:
    dict1[y]+=1
  except KeyError:
    dict1[y]=1

for a in sorted(dict1.iteritems(), key=lambda (k,v):(v,k), reverse=True):
  if a[1]>1:print a[0],a[1] 


