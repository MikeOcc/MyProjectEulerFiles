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
        #print s, n
        z=(n[0],n[1])
        if z in d:
          v=d[z]
          #print "zv",z,v
          vv=v +[n]
          #print "vv",vv
          d[z]=vv
        else:
          d[z]=[n]

 	  
print len(l)
print

for i in d:
  print i,d[i]
summ=0
for i in xrange(200):
  if l[i][0]==0:continue
  ed = l[i][1],	l[i][2]
  zz = len(d[ed])  
  summ += zz
  #zz = d[ed]
  # for zzz in zz:
    # print ed, l[i]+[zzz[2]],zzz
  
print 
print summ
#print d
