def p390(N1=10^10) :
   d1=defaultdict(list)
   N0,sm1=int((N1/2)**(1/2.0)),0
   for b0 in xrange(2,N0+1,2) :
      b2=b0*b0
      b3=b2*b0
      x0,y0,p0,q0,p1,q1=0,b0/2,2*b2+1,4*b0,b3+b0,2*b2+1
      while y0<=N1 :
         if x0:
            d1[x0].append((b0,y0))
            sm1+=y0
         x0,y0=p0*x0+q0*y0,p1*x0+q1*y0
      if b0 in d1 :
         for b1 in d1[b0] :
            (x0,y0)=b1
            while y0<=N1 :
               if x0>b0:
                  d1[x0].append((b0,y0))
                  sm1+=y0
               x0,y0=p0*x0+q0*y0,p1*x0+q1*y0
            (x0,y0)=b1
            x0=-x0
            while y0<=N1 :
               if x0>b0:
                  d1[x0].append((b0,y0))
                  sm1+=y0
               x0,y0=p0*x0+q0*y0,p1*x0+q1*y0
   return sm1
