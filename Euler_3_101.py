#
# Euler Problem 101
#
#


a=[];b=[];c=[];d=[];e=[];f=[];g=[];h=[];i=[];j=[];u=[]

for n in xrange(1,11):

  #u = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
  a.append(1) 
  b.append(682*n-681 )
  c.append(21461*n**2 + -63701*n +42241)
  d.append(1 - n + n**2 - n**3) 
  e.append(1 - n + n**2 - n**3 + n**4) 
  f.append(1 - n + n**2 - n**3 + n**4 - n**5) 
  g.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6) 
  h.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7) 
  i.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8) 
  j.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9) 
  u.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10)


  
print a
print b
print c
print d
print e
print f
print g
print h
print i
print j
print u

