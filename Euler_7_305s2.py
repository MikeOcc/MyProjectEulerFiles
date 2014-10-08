#
#
#
def e305(t,top,start=0,N=1):
   print "*",t,
   s=str(t)[::-1] 
   M=len(s) 
   if top<start: return 0
   low=10**(N-1)
   total=e305(t,top,start+9*N*low,N+1)
   for k in xrange(N):
      D={} 
      D2={} 
      a=min(N,M+k) 
      for r in xrange(k,a):
         D[r]=int(s[r-k])
      for r in xrange(a,min(2*N,M+k)):
         D2[r-N]=int(s[r-k])
      if len(D2)==N:
         continue
 
      w=(top-start)//N
      r=(top-start)%N
      if r==0:
         r=N
         w-=1
      if r>=(N-k): w+=1
      limit=min(low+w,10*low)
      cache={}
      N0=N
      def f(N,limit,carry=False,v=0):
         if limit<=0: return 0
         limit=min(limit,10**N)
         if N==0:
            return 1 if carry else 0
         key=(N,limit,carry)
         if key in cache: return cache[key]
         total=0
         m=N-1
         for d2 in range(10):
            if m in D2 and D2[m]!=d2: continue
            if carry and d2<9: continue
            d=(d2+1)%10
            if m not in D or D[m]==d:
               if carry or d2<9:
                  total+=f(N-1,limit-d*10**(N-1),True,v*10+d)
            if carry: continue
            d=d2
            if m not in D or D[m]==d:
               total+=f(N-1,limit-d*10**(N-1),False,v*10+d)
         cache[key]=total
         return total
      total+=f(N,limit)-f(N,low)
   return total


def e305bisect(t):      
      low=1
      high=10**14
      while high!=low:
         mid=(high+low)>>1
         if e305(t,mid+len(str(t))-1)>=t:
            high=mid
         else:
            low=mid+1
      return low
print sum(e305bisect(3**k) for k in range(1,13+1))