from time import time
sttm=time()
from euler import lprm1, gpft1
from itertools import izip
from gmpy import invert


def p365a(lm1=1000,lm2=5000,n1=18,k1=9) :
	def d2b(n1,b1=2) :
		'''
		Convert from base 10 to another base
		'''
		lb1=[]
		append=lb1.append
		while n1 :
			append(n1%b1)
			n1/=b1
		return lb1[::-1]

	def cmbm1(n1,k1,p1=1009) :
		'''
		C(n1,k1) % p1 where p1 is prime
		'''
		r1,r2=max(k1,n1-k1),min(k1,n1-k1)
		if not r2 : return 1
		nm1,dn1=1,1
		for j1 in xrange(r1+1,n1+1) : nm1=(nm1*j1)%p1
		for j1 in xrange(2,r2+1) : dn1*=j1#(dn1*invert(j1,p1))%p1
		dn1=invert(dn1,p1)
		return (nm1*dn1)%p1

	def cmbp1(n1,k1,p1) :
		'''
		C(n1,k1) % p1 where p1 is a prime and n1,k1 are really large
		'''
		l1,l2=d2b(n1,p1),d2b(k1,p1)
		ln1,ln2=len(l1),len(l2)
		l2=[0]*(ln1-ln2)+l2
		c1=1
		for j1,j2 in izip(l1,l2) :
			if j1<j2 : return 0
			else : c1=(c1*cmbm1(j1,j2,p1))%p1
		return c1%p1


	lp1=[p1 for p1 in lprm1(gpft1(lm1,lm2),lm1)]
	sm1,ln1,n1,k1=0,len(lp1),10**n1,10**k1
	lp2=[]
	append=lp2.append
	for p1 in lp1 : append(cmbp1(n1,k1,p1)%p1)
	for i1 in xrange(ln1-2) :
		p11,p12=lp1[i1],lp2[i1]
		for i2 in xrange(i1+1,ln1-1) :
			p21,p22=lp1[i2],lp2[i2]
			pr12=p11*p21
			for i3 in xrange(i2+1,ln1) :
				p32=lp2[i3]
				if p12 or p22 or p32 :
					# In lining CRT to boost up the speed
					p31=lp1[i3]
					pr1,sm0=pr12*p31,0
					if p12 : 
						pr23=p21*p31
						sm0+=p12*pr23*invert(pr23,p11)
					if p22: 
						pr13=p11*p31
						sm0+=p22*pr13*invert(pr13,p21)
					if p32 : sm0+=p32*pr12*invert(pr12,p31)
					sm0%=pr1
					sm1+=sm0 
	return int(sm1)


sm1=p365a()

print '\nThe sum  is ',sm1
print "\nTime taken ",time()-sttm," s"