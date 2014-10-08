#
#
#  Euler 365
#
#


def facmodp(n,p):

  residue = 1
  while n > 0:
    m= n % p
    for i in xrange(1, m+1):
      residue = (residue * i) % p
    n /=p
    if n % 2 > 0:
      residue = p - residue 
  return residue

print facmodp(10,7)



