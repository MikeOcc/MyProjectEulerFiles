


N = 10**6
print
print "calculating strong rep units for N<=",N,"..."
M={}
tot = 1
n = 1
while 1:
  rep = 2**n-1
  if rep>=N:break
  #tot+=rep
  print n,rep
  try:
    M[rep]+=1
  except KeyError:
    M[rep]=1
  n+=1

b=3
while b<N+1:
  print "base:",b

  rep = 1
  n=1
  while rep <= N:
    rep += b**n
    if rep>=N:
       break
    else:
       print n,rep
       try:
         M[rep]+=1
       except KeyError:
         M[rep]=1

    n+=1
  b+=1

#print 
#print M

print "############"
for key in M:

  if M[key]>1:
     print "!",key, M[key]
     tot +=key

print "Sum for all strong repunits is",tot
print