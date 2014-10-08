#Considering quadratics of the form:
#
#
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting #with n = 0.
#
#

from Functions import IsPrime

def consPrimes(a,b):

  numberofPrimes = 0

  stillPrime = True
  ctr = 0

  while stillPrime == True:
    x = ctr**2 + a*ctr + b
    if IsPrime(x):
      ctr+=1
    else:
      stillPrime = False
      break
  return ctr


if __name__ == '__main__':

  maxa , maxb = 0,0
  maxcons = 0

  for i in range(-1000,1000):
    for j in range(-1000,1000):
      if IsPrime(abs(i)) and IsPrime(abs(j)):
        cons = consPrimes(i,j)
        if cons>maxcons:
           maxcons = cons
           maxa , maxb = i,j
           print "new max found",i,j,cons
 
  print "For coefficients (a,b) = (",maxa,maxb,") we get",maxcons,"consecutive primes"

  for k in range(0,maxcons):
   print k+1,") " , k**2 + maxa*k + maxb

print
print "The product of the coefficients is:", maxa*maxb









