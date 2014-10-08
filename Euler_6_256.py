#
#
#
#
from math import floor
from Functions import RetFact
from itertools import combinations


def TataniFree(a,b):
#
#  If room is Tatani Free, return True
#
  
  #for numbers a <= b:
 
  if (a<=6) or (b<(a + 3)): 
    #not free = False
    return 0

  i = a-6
  j = floor((b-2) / (a+1)) - 1
  if (i-2*j) <= 0:
    return 0

  if (b-2)%(a+1) <= (i-2*j):
    #free = True
    return 1
  else:
    return 0



def RetDiv(f):
#
#  determine all combinations of prime factors
#
  #print f

  d2 = []
  
  l = len(f)
  for i in xrange(2,l):
    a = combinations(f,i)
    #print "i:",i
    for b in a:
      #print "b",list(b)
      v=1
      b = list(b)
      for x in xrange(len(b)):
         #print "*",b[x]
         v*=b[x]
      #print "v",v
      d2.append(v)     
      
  d2.append(1)
  for ff in f:
    d2.append(ff)
  #print d2
  
  return sorted(list(set(d2)))


################

# lazy, pick integers by hand
# N = 2 * 3 * 5 * 7 * 11 * 13 * 17  (25)
# N = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 (62)
# N = 2* 2 * 3 * 5 * 7 * 11 * 13 * 17 (41)
# N = 2* 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 (69)
# N = 2 * 2* 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 (93)
# N = 2 * 2* 2 * 3 * 5 * 5 * 7 * 11 * 13 * 17 (96)
# N = 2 * 2 * 2* 2 * 3 * 5 * 5 * 7 * 11 * 13 * 17 (126)
# N = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 11 * 13 * 17 (202)
# N = 2 * 2 * 2 * 2 * 2 * 2 * 3 * 5 * 5 * 7 * 11 * 13 * 17 (183)
N = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 7 * 11 * 13 * 17   #  (200)

facts = RetFact(N)

#print facts

divs = RetDiv(facts)

print
print divs
print

ctr=0
for a in divs:
  b = N/a
  if a <= b:
    
    if TataniFree(a,b):
      print "T Free, a,b:",a,b
      ctr+=1

print "T(",N,") =",ctr