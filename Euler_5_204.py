#
#  Euler 204
#


from Functions import RetFact,IsPrime,primes

pns = primes(10**9)

summ = 0
for i in xrange(2,10**9):
  if i> 100 and not (i in pns):continue

  zz = sorted(RetFact(i),reverse=True)
  if zz[0]<101:
    print i,zz[0]
    summ+=1


print
print "Hamming Number type 100 <10^9 is",summ+1
