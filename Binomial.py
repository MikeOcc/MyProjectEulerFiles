#
#  Binomial Functions.
#
#

def nCr(N,r):     # from scipy.comb(), but MODIFIED!  Binomial Functions.
    if (r > N) or (N < 0) or (r < 0):
        return 0L
    N,r = map(long,(N,r))
    top = N
    val = 1L
    while (top > (N-r)):
        val *= top
        top -= 1
    n = 1L
    while (n < r+1L):
        val /= n
        n += 1
    return val



if __name__=='__main__':
  
  for i in xrange(1,101):
   for j in xrange(1,101):
     if i>= j:
       print i,"choose",j,":",nCr(i,j)
