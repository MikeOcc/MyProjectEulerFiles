#
#
#  Euler Problem 133
#
#


from Functions import RofPrimes

def RepUnit(r):
  num = (10**r-1)/9

  return num

primes = RofPrimes(2,100000)

R =[]    #RepUnit(10**3)

for i in xrange(1,8):
  R.append(RepUnit(10**i))

summ = 0
for p in primes:
  isFactor = False
  for r in R:
  
    x = r/p
    if x*p == r:
      isFactor = True
  if isFactor == False:
    #print p
    summ += p


print
print "The Sum of Prime Never Factors is",summ






