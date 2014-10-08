from Functions import primes,RofPrimes

from math import factorial

def S(p):

  summ = 0

  for k in range(1,6):
      summ += factorial(p-k)

  summ = summ%p

  return summ




x = RofPrimes(5,100)

#print x

for z in x:
  print z,S(z)

