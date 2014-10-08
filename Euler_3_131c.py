#
#  Euler problem 131
#
#  []


from Functions import RofPrimes,IsPrime

#primes = RofPrimes(2,10**6)
#cubes = [i**3 for i in xrange(2,10**4)]

ctr=0
max = 0
for j in xrange(2,10**6):

  for i in xrange(j-1,0,-1):
      x = (j**3 - i**3)/float(i**2)
      if int(x)!=x:continue
      if x < max:break
      if IsPrime(int(x)) :  # in primes:
        print int(x), i, j
        ctr+=1
        max = int(x)
        break
  if max>1000000 or ctr> 172:break


print "total is", ctr






