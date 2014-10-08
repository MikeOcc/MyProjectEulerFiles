#
#
#  Euler Problem 282
#
#


def A(m,n):

  if m==0: 
     #print "1:", m,n+1
     return n+1

  if m==1:
     return (n+2)
	 
  if m==2:
     return (2*n + 3)

  if m==3:
     return (2**(n+3)-3)  

  if m==4:
     return towerMod(n) - 3
	 
	 
  if m>0 and n==0:
     #print "2:",m
     #print "A(",m-1,", 1)"
     return A(m-1,1)
  
  else:
     #print "3:",m,n
     #print "A(",m-1,", A(",m,", ",n-1,"))"
     return A(m-1,A(m,n-1))

def modpow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def towerMod(n):
#
#  Expoentiation va Euler's Method
#  Phi(14**8)->Phi(7**8) = 7**8*6/7 = 4941258
#
  if n>7:n=7
  n1=n+2
  x=2
  ctr=1
  while n1 >0:

    if n1==1:
      x=pow(2,x,14**8)	
    else:
      x=modpow(2,x,4941258)	
	
    n1-=1
    ctr+=1
  return (x)
  
# d={}

# for i in xrange(20):

  # z = towerMod(i)
  #print z
  # if z in d:
    # a=d[z]
    #print "A",a,z
    # d[z]=a+[i]
  # else:
    # d[z]=[i]

# for i in d:
  # z = d[i]
  # if len(z)>1:
    # print i,z  
  
	
#print modpow(2,modpow(2,pow(2,65536),14**8),14**8)-3
	
#print A1(3,4)
#print A1(4,2)
print A(6,0)
#print A1(4,4)
summ = 0
modval = 0
for n in xrange(6):
  modval = A(n,n)
  print n,modval
  summ += modval
  
print 6,A(5,5)

summ += A(5,5)
summ %= 14**8

print "The result is ", summ


