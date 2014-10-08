#
#  Euler 105
#


from string import whitespace,strip,replace
from itertools import combinations
from time import time

def ff(n):
  #  check to make sure that Sum(B)!=Sum(C) for len(B)=len(C).  Sorting is irrelevant here since we have to consider
  #  number combinations that are not necessarily in numerical order.  I only implemented this after I realized
  #  that the clunky code in the main body was only finding a small portion of the non special sets.  I know this is
  #  lazy, I should have just generated each subset, ordered and checked for consecutive equal values.
  l = len(n)

  for w in xrange(2,l/2 + 1):
    aa = combinations(n,w)
  
    for aaa in aa:
      bb = combinations(n,w)
      for bbb in bb:
         if aaa != bbb:
             if sum(aaa) == sum(bbb): 
                #print "found"
                return False
  
  return True

st = time()

f = open('sets.txt','r') 

summ=0

print 
print "These are the sets that are Special Sums..."

for i in range(0,100):      #for a in x:
  x= replace(strip(f.readline()),","," ")
  z = x.split(" ")    # I wish I knew how to split the string directly into integers. I figured it out earlier and forgot
  v=[]
  for a in z:
    v.append(int(a))
    v = sorted(v)
  
  l = len(v)

  if ff(v)==False:continue    #  check to see that subsets of equal length do not have equal sums

  # now that each set is sorted, check to see if the S(B)>S(C), len(B)>len(C) rule is met.  This is ugly code but 
  # faster than resorting to combinatorics again.  Thanks to sorting only need to compare the smallest sum of B to
  # the greatest sum of C.   
  if not (v[0]+v[1] > v[l-1]):  
    continue
  elif not (v[0]+v[1]+v[2] > v[l-2]+ v[l-1]):
    continue
  elif not (v[0]+v[1]+v[2]+v[3] > v[l-3]+v[l-2]+ v[l-1]):
    continue
  elif l> 7 and (not (v[0]+v[1]+v[2]+v[3]+v[4] > v[l-4]+v[l-3]+v[l-2]+ v[l-1])) or (not (v[1]+v[2]+v[3]+v[4] > v[l-3]+v[l-2]+ v[l-1])):
    continue
  elif l> 10 and not (v[0]+v[1]+v[2]+v[3]+v[4]+v[5] > v[l-5]+v[l-4]+v[l-3]+v[l-2]+ v[l-1]):
    continue
  elif l==12 and not (v[1]+v[2]+v[3]+v[4]+v[5] > v[l-4]+v[l-3]+v[l-2]+v[l-2]):
    continue
  else:
    subsum = sum(v)
    print v,":", subsum
    summ += subsum

print
print "Total of Special Sum Sets is", summ
print "Process time is", time() - st
f.close()

