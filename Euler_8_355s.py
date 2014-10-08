from math import *
from Functions import RetFact
n=200000
n2=int(sqrt(n))
prime=[0]*(n+1)
primes=[]
for i in xrange (2,n2):
    if prime[i] == 0:
        for j in xrange (2*i,n+1,i):
            prime[j]=1
for i in xrange (1,n):
    if prime[i]==0:primes.append(i)
def prev_prime(n):
    for i in range(100):
        if prime[n-i]==0:
            return n-i
i=1
pairs=[]
while primes[i]<n2:
    pairs.append([primes[i],0])
    i+=1
pri=primes[i]
for i in range(len(pairs)):
    if pairs[i][0]**2*pri<n:
        maxp=0
        for e in range(2,20):
            pe=(pairs[i][0]**e)
            if pe>pri:break
            m=n/pe
            p=prev_prime(m)
            pep=pe*p-p
            if pep>maxp:
                maxp=pep
                pm=p
        pairs[i][1]=pm
        prime[pm]=1
    else:
        pairs[i][1]=prev_prime(n/pairs[i][0])
        if prime[pairs[i][1]]==1:
            pairs[i][1]=prev_prime(pairs[i][1]-1)
        prime[pairs[i][1]]=1
sw=1
while sw>0: 
    sw=0
    for i in range(len(pairs)-2):
        if sw==1:break
        if pairs[i][0]**2*pairs[i][1]<n:continue
        p11=pairs[i][0]
        p12=pairs[i][1]
        d1=p11*p12
        for j in range(i+1,len(pairs)-1):
            p21=pairs[j][0]
            p22=pairs[j][1]
            d2=p21*p22
            d11=p11*p22
            d12=p21*p12
            if d11+d12>d1+d2 and d11<n and d12<n:
                pairs[i][1]=p22
                pairs[j][1]=p12
                sw=1
                break
co=0
for i in range(len(pairs)):
    prime[pairs[i][0]]=1
    prime[pairs[i][1]]=1
    for j in range(1,10):
        if pairs[i][0]**j*pairs[i][1]>n:break
        else: d=pairs[i][0]**j*pairs[i][1]
    print d,pairs[i][0],j,pairs[i][1] 
    co+=d
for i in range(n):
    if prime[i]==0:
       #print i,RetFact(i)
       co+=i
print

print co