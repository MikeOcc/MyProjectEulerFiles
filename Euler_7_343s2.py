def euler343c(N=2*10**6):
   L=N+2
   M=[0]*L 
   MF=[1]*L
   A=[0]*L 
   AF=[1]*L 
   for k in xrange(1,L):
      M[k]=k
      A[k]=k*k-k+1    
   for k in xrange(1,L):
      p=M[k]
      if p>1:
         for x in xrange(k,L,p):
            while M[x]%p==0: M[x]/=p
            MF[x]=p
      p=A[k]
      if p>1:
         for x in xrange(k%p,L,min(L,p)):
            while A[x]%p==0: A[x]/=p
            AF[x]=max(AF[x],p)
         for x in xrange(min(L,(1-k)%p),N+1,min(L,p)):
            while A[x]%p==0: A[x]/=p
            AF[x]=max(AF[x],p)
   print sum(max(MF[k+1],AF[k])-1 for k in xrange(1,N+1))


from time import time
st=time()
euler343c()
print "process time is",time()-st