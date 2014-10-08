#
# Problem 113
#


def binomial(n, k):
  nt = 1
  for t in range(min(k, n-k)):
    nt = nt*(n-t)//(t+1)
    #print "@:", nt
  return nt

def binomialCoefficient(n, k):
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i)
        c = c / (i + 1)
    return c

print binomial(6,2)

n=6  #100
#print binomial(n+10,10) + binomial(n+9,9) - 10*n - 2
print binomial(n+10,10) + binomial(n+9,9) - 10*n - 2

print  binomial(n+10,10) , binomial(n+9,9) , 10*n - 2 
n=100
print  binomialCoefficient(n+10,10) + binomialCoefficient(n+9,9) - 10*n - 2