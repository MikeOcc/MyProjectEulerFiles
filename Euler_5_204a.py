#
#  Euler 204
#


from Functions import RetFact,IsPrime,primes
print "counting primses..."
#pns = primes(10**9)

print "primes calculated..."

summ = 99
for i in xrange(100,10**9+1):
  #if (i in pns):continue

  zz = RetFact(i)
  if max(zz)> 100:continue
  
  #print i,zz
  summ+=1


print
print "Hamming Number type 100 <10^9 is",summ+1
