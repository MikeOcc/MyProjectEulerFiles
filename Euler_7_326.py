#
#
#  Euler Problem 326
#
#




def a(n):
  if n==1: return 1
  a=[]
  a.append(0)
  a.append(1)
  summ = 0
  for k in xrange(1,n):
    anext = k * a[k]
    a.append(anext)
    
    #summ += 
  return 0


#  a2 = 1*a1 mod 2 = 1
#  a3 = (1*a1 + 2*a2) mod 3 = 0
#  a4 = (1*a1 + 2*a2 + 3*a3) mod 4 = 
a=[]
a.append(0)
a.append(1)
summ = 1
for i in xrange(2,11):
  z=0
  for k in xrange(1,i):
    z += k * a[k]
  a.append(z%(i))
  summ +=k*(z%i)
  print i,z,z%i,summ,summ%(i+1)
print a

print
summ = 0
for i,j in enumerate(a):
  if i==0:continue
  if i==1:
    summ=1
  summ+=i*j
  print i,j,i*j,summ%i
