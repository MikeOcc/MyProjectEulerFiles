#
#
#
#
from time import time

def isPal(n):
  ns = str(n)
  return ns == ns[::-1]

st = time()
tally = {}
cubeso = []
squareso = []
cubese = []
squarese = []
# brutish force. trying squares and cubes up to a billion.  would have pushed the numbers up if needed, but was not necessary.

for i in xrange(1,1002,2):
  cubeso.append(i**3)

for i in xrange(2,1002,2):
  cubese.append(i**3)

for i in xrange(1000,30000,2):
  squarese.append(i**2)

for i in xrange(1001,30000,2):
  squareso.append(i**2)


for c in cubeso:
  for s in squarese:
    h = s + c
    # Palindromes that fit the bill must be odd.  
    if isPal(h):
      if tally.has_key(h):
        tally[h]+=1
        #print "Bingo",h,s**.5,c**(1/3.)
      else:
        tally[h]=1

for c in cubese:
  for s in squareso:
    h = s + c
    # Palindromes that fit the bill must be odd.  
    if isPal(h):    # this line changed, no longer needs *odd* check
      if tally.has_key(h):
        tally[h]+=1
        #print "Bingo",h,s**.5,c**(1/3.)
      else:
        tally[h]=1

summ = 0
print
kys = tally.keys()
for a in kys:
  if tally[a]==4:
    print a, tally[a]
    summ += a


print
print "sum is", summ
print "process time is", time()-st
