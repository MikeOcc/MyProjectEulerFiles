#
# Euler 37
#  find the sum of the only truncatable primes
#
from Functions import IsPrime

def IsTruncatable(num):
  
  ntrunc = True

  nstr = str(num)
  nlen = len(nstr)

  for i in range(0,nlen):
    if not IsPrime(int(nstr[i:])): return False
    if not IsPrime(int(nstr[:i+1])): return False

  return True


if __name__ == '__main__':

  numtrunc = 0
  numtrunclist=[]
  ctr = 23

  while numtrunc < 11:

     if IsPrime(ctr) and IsTruncatable(ctr):
        numtrunclist.append(ctr)
        numtrunc +=1
        print ctr
        print numtrunc
     
     ctr +=1
     if ctr%2==0: ctr+=1

        
print numtrunclist
print sum(numtrunclist)


  