

def A1(m,n):

  if m==0: 
     #print "1:", m,n+1
     return n+1
  
  if m>0 and n==0:
     #print "2:",m
     #print "A(",m-1,", 1)"
     return A1(m-1,1)
  
  else:
     #print "3:",m,n
     #print "A(",m-1,", A(",m,", ",n-1,"))"
     return A1(m-1,A1(m,n-1))
  

def A(m, n):
  s = [m];
    #s.add(m);
  while (s!=[]):
    m=s.pop()
    if(m==0 or n==0):
       n+=m+1
    else:
       m-=1
       s.append(m)
       m+=1
       s.append(m)
       
       n-=1
  
  return n

def modpow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


print modpow(2,modpow(2,pow(2,65536),14**8),14**8)-3
	
#print A1(3,4)
print A1(3,3)

