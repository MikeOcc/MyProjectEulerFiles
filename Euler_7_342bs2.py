from Functions import RetFact

def tsearch(n,tnn,needed,qi,fcs):

#Search for solutions given some stem, recursively
  print n,tnn,needed,qi,fcs
  global primsol
  #Try each prime less than primes[qi], in descending order.
  for qj in xrange(qi-1,-1,-1):
    q=primes[qj]
    if n*q<maxsol:
        tnn2={}
        for k in tnn.keys():
          tnn2[k]=tnn[k]
        if not tnn2.has_key(q):
          n2=n*q*q
          tnn2[q]=3
        elif tnn2[q]%3==0:
          n2=n*q*q
          tnn2[q]+=3
        elif tnn2[q]%3==2:
          n2=n*q
          tnn2[q]+=1
        elif tnn2[q]%3==1:
          n2=n*q**3
          tnn2[q]+=5
        for p in f[q-1]:
          if tnn2.has_key(p):
            tnn2[p]+=1
          else:
            tnn2[p]=1
        needed2=1
        maxpneeded=1
        for p in tnn2.keys():
          if tnn2[p]%3!=0:
            needed2*=p**(3-tnn2[p]%3)
            if p>maxpneeded:
              maxpneeded=p
        if n2*maxpneeded<maxsol:
          if needed2==1:
            primsol[n2]=fcs+[q]
          print "*"
          tsearch(n2,tnn2,needed2,qj,fcs+[q])
 



primes=[2]
maxsol=10**10
maxp=int(maxsol**0.5)
f=[[],[],[2]]
#Generate all primes up to maxp as potential largest primes in the solution
#Generate factorizations to be used later.
for i in xrange(3,maxp+1):
  for p in primes:
    if i%p==0:
      f.append([p]+f[i/p])
      break
    if p*p>i:
      #print p,i
      primes.append(i)
      f.append([i])
      break

 
#Store primitive solutions and all their unique prime factors
primsol={}
 
#Search for solutions with given largest prime
for qi in xrange(len(primes)):
  q=primes[qi]
  #initial candidate solution - largest prime must be squared
  n=q**2
  #totient of n^2
  tnn={}
  tnn[q]=3
  for p in f[q-1]:
    if tnn.has_key(p):
      tnn[p]+=1
    else:
      tnn[p]=1
  needed=1
  maxpneeded=1
  for p in tnn.keys():
    if tnn[p]%3!=0:
      needed*=p**(3-tnn[p]%3)
      if p>maxpneeded:
        maxpneeded=p
  if needed==1:
    primsol[n]=[q]
  if n*maxpneeded<maxsol and q>maxpneeded:
    tsearch(n,tnn,needed,qi,[q])
 
#Search for extensions of these solutions by multiplying by a cube of a factor
sols=[]
print
print primsol
print
for s in primsol.keys():
  print "!",s, RetFact(s)
  totest=[s]
  for p in primsol[s]:
    mt=len(totest)
    for i in range(mt):
      j=3
      while totest[i]*p**j<maxsol:
        totest.append(totest[i]*p**j)
        j+=3
  print "!!",s,totest
  sols+=totest
print
print sorted(sols)
print sum(sols)