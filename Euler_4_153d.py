#
#
#
#
from Functions import gcd
from time import time
summ=0;
Lim=100000
st=time()
for i in xrange(1,Lim+1): #        for(int i=1;i<=Lim;i++)  
  summ+=(Lim/i)*i

for a in xrange(1,int(Lim**.5)+1):   #(int a=1;a*a<Lim;a++)
  for b in xrange(1,a+1):   #(int b=1;b<=a /*&& (a*a+b*b)<=Lim*/;b++) 
    if (gcd(a,b)==1): 
       div=(a*a+b*b)
       if (a==b):
          val = (a+b)
       else:
          val=2*(a+b);
       for j in xrange(1, Lim/div +1):       #(int j=1;i*j<=Lim;j++) :
         summ+=(j*val*(Lim/(div*j)))

		 
print summ
print time()-st