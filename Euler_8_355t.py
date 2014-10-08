


S=[]
S.append(3)

a = 2

for n in xrange(1,11):
  tmp = a + S[n-1]*(S[n-1]-a)
  print a,tmp
  S.append(tmp)


print S