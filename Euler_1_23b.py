
def d(n):
  from math import floor,sqrt

  #print n,

  if n==1: return 0 
  else:
     sum1=1+r 
     r=r-1 
  else:
     sum1=1

  if float(n)/2. != n/2 :
     f=3; step=2
  else:
     f=2; step=1

  while f<=r:
       sum1+= f+ (n/f)

  #print sum1


def abundantsum(i): 
  return any(i-a in abundants for a in abundants) 


if __name__ == "__main__":

  abundants = set(i for i in range(1,28124) if d(i) > i) 

  print sum(i for i in range(1,28124) if not abundantsum(i))



