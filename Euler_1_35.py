from Euler_Prime import IsPrime


num = 0

for i in range( 2, 1000000):  ##0000

   if IsPrime(i):
 
      xx = str(i)
      xlen = len(xx)
      iscirc = True
      for j in range(1,xlen+1):
        xx=xx[1:]+xx[:1]
        if IsPrime(int(xx))==False:
           iscirc = False
      if iscirc:
        num += 1


print "# of Circular Primes is ", num
