#
# Euler Problem 72
#
#

L = 1000000 + 1
phi = range(L)
for n in range(2, L):
  if phi[n] == n:
    for k in range(n, L, n):
      phi[k] *= (n - 1.)/n;
 
print "Answer is", int(sum(phi)-1)











