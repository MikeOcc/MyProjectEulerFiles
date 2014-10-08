from itertools import count
from math import sqrt
 
x = 0
for a in count(1):
	print a,":"
	for s in range(2, 2*a):
		#print "*",
		z = sqrt(a**2+s**2)
		if int(z) == z:
			if s==(2*a)-1:print "!!!!",
			t = min(a, s-1)-(s-1)/2
			print a,s,t
			x += t
	print
	if x > 1000000:
		print a, x
		exit()