#
#
# gk = 1, for 0  k  1999
# gk = gk-2000 + gk-1999, for k  2000.
# Find gk mod 20092010 for k = 1018.
#2,3,5
#
M= 20092010
"""
fibo = 0
f =[]
for i in xrange(2000):
  f.append(1)
f1,f2 = 1,1
temp=f[1]
for k in range(2000,32000):

    fibo = f[k%2000] + temp
    f[k%2000]=fibo
    
    temp=f[(k+1)%2000]
    print k,fibo
""""

n=10**18
#lagged fibo =
f = pow(2,(n/2000)-1,M) 

print
print "##########################"
print
print "Answer is ", f