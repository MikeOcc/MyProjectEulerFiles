#
#
# Euler Problem 134
#
#


from Functions import primes


def ext_gcd(a,b):
  s,s0=0,1
  t,t0=1,0
  r,r0=b,a
  while r != 0:
    q = r0/r
    r0,r = r,r0-q*r
    s0,s = s,s0-q*s
    t0,t = t,t0-q*t
    # print q,r,r0,s,s0,t,t0
  # print "bezouts coeffs", s0,t0
  # print "gcd ", r0
  # print "quots by the gcd", t,s
  return r0
  
print ext_gcd(240,46)

exit()


p = primes(1000000)


l = len(p)
summ=0

for i in xrange(2,l-1):

  j = i+1
  v1 = p[i]
  l1 = len(str(v1))
  base = 10**l1
  inc = 1
  #	print v1, base,inc, p[j]
  while True:
    ctr=base*inc
    v2 = ctr+v1
    if v2/p[j]== float(v2)/p[j]:
      #print i,p[i],p[j],v2
      break
    inc +=1
    summ+=v2
	
	
print "The sum is", summ
	  