#
# problem 267
#
#


def fac(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a
 
N = 1000
n_fac = fac(N)

T = 0

for i in range(432):
    T += n_fac/fac(i)/fac(1000-i)
 
print 1 - T*1.0/2**1000