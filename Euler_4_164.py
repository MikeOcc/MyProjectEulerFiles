#
#
#  Euler 164
#
#


l=[]
d={}
for i in xrange(10):
  for j in xrange(10):
    for k in xrange(10):
      n = [i,j,k]
      s = sum(n)
      if s<10:
        l.append(n)
        print s, n
        z=(n[1],n[2])
        if z not in d:
          d[z]=[n]
        else:
          v=d[z]
          print "n ",z,n,v
          try:
            v=v.append(n)
          except:
            v=[n]
          d[z]=v	  
print len(l)


for i in xrange(200):
  ed = l[i][2]
  print ed
  
print 
print d
