#
#  find maximal sum in triangle.txt
#

#from os import curdir
from string import whitespace,strip,replace
#from operator import mul
#from array import array
#from math import *
from itertools import combinations
def ff(n):

  l = len(n)

  for w in xrange(2,l/2 + 1):
    aa = combinations(n,w)
  
    for aaa in aa:
      #print "%", aaa
      bb = combinations(n,w)
      for bbb in bb:
         if aaa != bbb:
             #print "!@!",n,aaa,sum(aaa),bbb,sum(bbb)
             if sum(aaa) == sum(bbb): 
                print "found"
                return False

  '''
  for w in xrange(2,l/2):
    aa = combinations(n,w)
  
    for aaa in aa:
      #print "%", aaa
      bb = combinations(n,w)
      for bbb in bb:
         if aaa != bbb:
             #print "!@!",n,aaa,sum(aaa),bbb,sum(bbb)
             if sum(aaa) == sum(bbb): 
                print "found"
                return False
  '''

  return True
#curdir = "/python"

f = open('sets.txt','r') # Number pasted to file.

summ=0
ctr=0
summ2=0

#x=f.readlines()

for i in range(0,100):      #for a in x:
  x= replace(strip(f.readline()),","," ")
  z = x.split(" ")
  v=[]
  for a in z:
    v.append(int(a))
    v = sorted(v)
  
  l = len(v)
  print i,l,"#"
  summ2+=sum(v)

  if ff(v)==False:continue

  if not (v[0]+v[1] > v[l-1]):  
    print "!ooops!",v
    continue
  elif not (v[0]+v[1]+v[2] > v[l-2]+ v[l-1]):
    print "ooops",v
    continue
  elif not (v[0]+v[1]+v[2]+v[3] > v[l-3]+v[l-2]+ v[l-1]):
    print "ooops!",v
    continue
  elif l> 7 and (not (v[0]+v[1]+v[2]+v[3]+v[4] > v[l-4]+v[l-3]+v[l-2]+ v[l-1])) or (not (v[1]+v[2]+v[3]+v[4] > v[l-3]+v[l-2]+ v[l-1])):
    print "ooops!!",v
    continue
  elif l> 10 and not (v[0]+v[1]+v[2]+v[3]+v[4]+v[5] > v[l-5]+v[l-4]+v[l-3]+v[l-2]+ v[l-1]):
    print "ooops!!!",v
    continue
  elif l==12 and not (v[1]+v[2]+v[3]+v[4]+v[5] > v[l-4]+v[l-3]+v[l-2]+v[l-2]):
    print "ooops!!!!",v
    continue
  else:
    print v
    summ += sum(v)

print "total is", summ
print "total is", summ2
f.close()

