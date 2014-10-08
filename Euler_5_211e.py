
def listSigma2(n):
  
  sqrt = (int(n**.5)) 
  
  quasiPrimeFactor = [0]*(n + 1)
  
  for i in range(2,sqrt+1):   #(int i = 2; i <= sqrt; i++):
  
    if quasiPrimeFactor[i] == 0:
      quasiPrimeFactor[i] = i
      if (i * i) <= n :
        for j in range(i*i,n+1,i):   #(int j = i * i; j <= n; j += i) :
          if quasiPrimeFactor[j] == 0:
            quasiPrimeFactor[j] = i
   
  sigma2 = [1]* (n + 1)
  sigma2[1] = 1;
  #print quasiPrimeFactor;
  
  for i in range(2, len(sigma2)):
    p = quasiPrimeFactor[i];
    if p == 0:
        p = i
    summ = 1
    j = i
    p2 = p * p
  
    #for k in range(p2, i, p2):  #(long k = p2; j % p == 0; j /= p, k *= p2)
    k = p2 
    while 1:   	
      dobreak = (j%p==0)
      summ += k
      j /= p
      k*=p2
      if dobreak:
         break

    print "summ:",summ
    sigma2[i] = summ * sigma2[j]
    
  return sigma2


def isPerfectSquare(x):

  #if not isResidue[(int)(x % RESIDUE_TEST)] :
  #  return False
  #print x
  if int(x**.5)**2 == x:
    return True
	
    # long y = 0;
		# for (long i = 1L << 31; i != 0; i >>>= 1) {
			# y |= i;
			# if (y > 3037000499L || y * y > x)
				# y ^= i;
		# }
		# return y * y == x;
	# }




LIMIT = 44;

RESIDUE_TEST = 3 * 5 * 7 * 11 * 13;

isResidue = [0]*RESIDUE_TEST

for i in range(RESIDUE_TEST):

  isResidue[i * i % RESIDUE_TEST] = True

sigma2 = listSigma2(LIMIT - 1)

print sigma2
print LIMIT

sum1 = 0;

for i in range( 1, LIMIT ):

  gg = sigma2[i]
  print "gg", gg
  if (isPerfectSquare(gg)):
    sum1 += i;

print "The sum is", sum1