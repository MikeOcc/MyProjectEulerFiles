#
#  Euler 204
#

from sets import Set
from math import log10, ceil

from Functions import RetFact,IsPrime,primes
print "counting primses..."
#pns = primes(10**9)

p = primes(100)

print "primes calculated..."

summ = 0
s = {1}
maxpow = 9
uplim = 10**maxpow

for i in p:
   #print i 
   lim = int(ceil(log10(10**maxpow)/log10(i)))
   l = []
   for x in s:
      for j in range(lim):
	    num = i ** (j + 1) * x
	    #print num,RetFact(num)
	    if num > uplim: break
	    l = l + [num]
   s = s | set(l)
	   
   
   
print "length of set is ", len(s)
   
  
  
  
  




print
#print "Hamming Number type 100 <10^9 is",summ+1
