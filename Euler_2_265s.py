def e265_recurse(S,last,N):
   if len(S)==N:
      return last
   last*=2
   t=last&(N-1)
   s=0
   if t not in S:
      S.add(t)
      s+=e265_recurse(S,last,N)
      S.remove(t)
   t+=1
   if t not in S:
      S.add(t)
      s+=e265_recurse(S,last+1,N)
      S.remove(t)
   print s
   return s
 
def euler265(n):
   print e265_recurse(set([0]),0,2**n)/2**(n-1)

euler265(5)