

from Euler_Prime import IsPrime

def SmallestNumber(n):
  from Euler_Prime import IsPrime
  #from math import sort
  smallestnum = 1

  factlist = [1]

  # first gather all primes <= n

  for i in range(1,n+1):
    if IsPrime(i):
       factlist.append(i)
       zz = i
       smallestnum *= zz
    else:
       temp = float(smallestnum)/float(i)
       if temp != int(temp):
         print "oops",i, smallestnum, temp
         y = (temp - int(temp))          
         zz = int(round(1.0/y,2))
         print "zz",zz,y
         factlist.append(zz)
         smallestnum *= zz
  if zz != n:factlist.append(n)
  #factlist.sort()
  print "Smallest Number that can be divided by Range(1,",n,") is", smallestnum
  print ""
  #print factlist
  factlist.sort()
  print factlist

if __name__ == "__main__":
  
   #for j in range(10, 100):
     print SmallestNumber(27)

