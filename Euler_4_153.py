#
#  euler problem 153
#
#
from Functions import gcd
Lim = 10000  #100000000

d={}
sum=0
z=0
for i in xrange(1,Lim+1):

   sum+=(Lim/i)*i;

   for a in xrange(1,int(Lim**.5)+1):
      for b in xrange(1,a+1):     # /*&& (a*a+b*b)<=Lim*/;b++)
         if (a,b) in d:
           z = d[(a,b)]
         else:
           d[(a,b)]=gcd(a,b)
		 
         if(z==1):
            i=(a*a+b*b)
            if (a==b):
               val=(a+b)
            else:
               val=2*(a+b);

            for j in xrange(1,int(Lim/i)+1):
                sum+=(j*val*(Lim/(i*j)));

print sum
