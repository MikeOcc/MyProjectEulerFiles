#
#
# Euler Problem 153
#
#
from time import time
from math import floor
from Functions import divisors,gcd
st=time()

N = 10**8
limit = int(N**.5)
#ctr = 1

summ=0
summ2=0
for a in xrange(1,limit+1):
  for b in xrange(a,limit+1):
    if gcd(a,b)!=1:continue
    #a2,b2=pow(a,2),pow(b,2)
    a2,b2=a**2,b**2
    div = a2 + b2
    if div>N:break
    #ctr+=1
    #No need for floor func. Runs slow, Int div in Python defaults to floor
    #Np=floor(N/div)
    if a==b:
      z=(a<<1)	
    else:
      z=(a+b)<<1
	  
    # num0=div=(a^2+b^2)  -> (num0, 2num0, 3num0....n*num0)/(div) == complex divisors
	# then take multiples of div, recalc floor and sum again
    for n in xrange(1, N/div +1):  
      #Np=(N/(div*n))
      #y=(n*z*(N/(div*n)))	
      summ+=(n*z*(N/(div*n)))
      #if a==1 and b==7:
        #print a,b,div,":",n,div*n,(N/(div*n)),":",y
        #summ2+=y
    #summ +=((a+b)*Np*(Np+1))
    #summ +=((a+b)*N*(N+1))/(2*div**2)
    #print a,b,":",div

# summ+=1  # flaw in divisors gives divisors(1)=[1,1]
# for i in xrange(2,100001):
  # d=divisors(i)
  # summ +=sum(d)

# slick way to sum divisors
#for i in xrange(1,N+1): #        for(int i=1;i<=limit;i++)  
#  summ+=(N/i)*i

summ3 = N**2
for i in xrange(1,N+1): #        for(int i=1;i<=limit;i++)  
  summ3-=N%i
summ+=summ3
  
print
print summ
print "time elapsed is", time()-st
print summ2