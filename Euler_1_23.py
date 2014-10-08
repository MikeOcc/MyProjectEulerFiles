#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
#as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
# greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#

#from Functions import IsPrime


def FactorN(n):

  from Functions import IsPrime
  if IsPrime(n): return [1]

  Facts=[1]

  if float(n)/2.0==n/2:
     endrange = n/2 + 1
  else:
     endrange = int(round(n**0.5,2)) + 1
  #ctr=0
  for i in range(2, int(n/2) + 1):
     if n%i==0:
       #ctr+=1
       Facts.append(i)

  return Facts

def SumofFacts(Factors):
  
  return sum(Factors)  

def IsAbundant(n):
  #
  #  determine if n is abundant
  #
  #return SumofFacts(FactorN(n))>n
   return SumOfProperDivisors(n)>n

#Second, improved version:
def SumOfProperDivisors(n):
  from math import floor,sqrt

  #print n,

  if n==1: return 0 
  else:    r=floor(sqrt( n) )   # first take into account the case that n is a perfect square.  if r*r==n:
     sum1=1+r 
     r=r-1 
  else:
     sum1=1

  if float(n)/2. != n/2 :
     f=3; step=2
  else:
     f=2; step=1

  while f<=r:     if n%f==0:
       sum1+= f+ (n/f)     f+= step

  #print sum1  return sum1

#_______________________

if __name__ == '__main__':

   from time import time
   sttime=time()
#
#  gather list of abundant numbers
#
#  print SumofFacts(FactorN(12))

   Abundants=[]

   for i in range(12 , 28124):
     if IsAbundant(i): Abundants.append(i)

   ALen = len(Abundants)

   Abundants.sort()
   print Abundants
   print 

   #exit()

   SumAbundants=[]

   for i in xrange(ALen):
     for j in xrange(ALen/2): 

        x = Abundants[i] + Abundants[j]

        if x<28124:
          SumAbundants.append(x)

   SumAbundants = list(set(SumAbundants))
   SumAbundants.sort()
   #print len(SumAbundants)      
   #print SumAbundants

   #exit()
   print

   Alen2 = len(SumAbundants)
   
   sum1 = sum(xrange(28124))
   sum2 = sum(SumAbundants)

   SoAPI = sum1 - sum2

   print "The sum of all positive integers which cannot be written as the sum of two abundance numbers is", SoAPI
   print "The process time is",time()-sttime

  


