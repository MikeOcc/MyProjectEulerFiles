

def A1(m,n):

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
     return tower(n) 
	 
	 
  if m>0 and n==0:
     #print "2:",m
     #print "A(",m-1,", 1)"
     return A1(m-1,1)
  
  else:
     #print "3:",m,n
     #print "A(",m-1,", A(",m,", ",n-1,"))"
     return A1(m-1,A1(m,n-1))

def modpow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def tower(n):
  if n>8:n=8
  n1=n+2
  x=2
  ctr=1
  while n1 >0:

    if n1==1:
      x=pow(2,x,14**8)	
    else:
      x=modpow(2,x,7**8-7**7)	
	
    n1-=1
    ctr+=1
  return (x -3)%14**8
  
# d={}

# for i in xrange(20):

  # z = tower(i)
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
print A1(6,1)
#print A1(4,4)

