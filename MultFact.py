#
#
#  adjunct to test multiplying primes
#
#

from Functions import RetFact,RofPrimes

# [2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]


#a = [2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 11, 13, 17, 19, 23, 29, 31,37]

a = [2, 2, 2, 3, 3, 3, 5, 5,  7, 7, 11, 13, 17, 19, 23, 29, 31, 37]


#primes = RofPrimes(2,60)

n=1
for b in a:
  n*=b


x = a   #RetFact(n)
s = set(x)
facts = []
for f in s:
    facts.append(x.count(f)*2+1)
m=1
for f in facts:
    m*=f
m+=1
m/=2


print m, facts
print
print n
