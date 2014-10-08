#
#
#  Euler Problem 239
#
#
from Functions import primes


def enumP(n) :

  #p=[i for i in xrange(101)]
  p=[1]
  for i in xrange(1,n+1):  #var i : uint = 1;i <= n;i++){
     p0 = 1.0
     fact =1.0
     for k in xrange(1,i+1): #var k : uint = 1;k <= i;k++){
       fact *= k
       p0 -= p[i-k]/fact
                    
     #p[i]=p0
     p.append(p0)
  
  return p

l = enumP(100)  #[i for i in xrange(101)]

print l

summ = 0

n = (((1./98.)/99.)/100.)



for k in xrange(76):
  if k >0:
  
    n*= 1.0 /(97-k+1)*(75-k+1)/k
  summ += l[97-k] * n

print (25.*24*23/3/2/1)*summ
	
  
  


 # var ps : Array = enumP(100);
# //                tr(ps.join('\n'));
            # // ret=C(25,3)*S_[k:0~75] p(97-k,0)*(97-k)!/100!*C(75,k)
            # // ????
                # var sum : Number = 0;
                # var base : Number = 1/98/99/100;
                # for(var k : uint = 0;k <= 75;k++){
                    # if(k > 0)base *= 1.0 / (97-k+1)*(75-k+1)/k;
                    # sum += ps[97-k]*base; 
                # }
                
                # return 25*24*23/3/2/1*sum;