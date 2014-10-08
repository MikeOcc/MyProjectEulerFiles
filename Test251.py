
lim = 110000000
for i in xrange(1,6000):
  a = i * 3 -1
  f = (i**2) * (8*i -3)

  print i,") ",a,":",f
    

  if f > lim:
    break
    #b=1;c=f
    #if a + b + c > lim:continue
    #ctr+=1
    #print a, b,c,":",a+b+c,ctr
    