

N=5000

a,b=1,7
summ2=0
z = a**2 + b**2
l = N/z

# for n in xrange(1,N/z+1):

  # div = N/(n*z)
  # if div==0:break

  # summ=0
  # for i in xrange(1,N/(n*(a**2+b**2)+1):
    # summ += (n*a+n*b) * 2
  
  # print n,div,((a*n)**2+(n*b)**2),summ
  # summ2+=summ
  
# print "tot",summ2



#  (n*a+n*b) * 2
#   2 * (a+b) * n * div
#   2 * (a+b) * n * (N/(n*z))

for n in xrange(1,l+1):

  div = N/(n*z)
  if div==0:break

  summ = 2 * (a+b) * n * (N/(n*z))
  
  print n,div,((a*n)**2+(n*b)**2),summ
  summ2+=summ
  
print "tot",summ2
