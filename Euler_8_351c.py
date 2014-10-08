





def numdots(m,x):
  y = m * x
  return y

N=5
m = 5/1000.
summ = 0
for j in xrange(1,3):
  m = float(j)/float(N)
  for i in xrange(1,N+1):
    z = numdots(m,i)
    if z==int(z):
      print j,i, z
      summ +=z

print summ