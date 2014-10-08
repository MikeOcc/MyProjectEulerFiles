from time import time
st=time()
def Roman2int( R ):
    w = [ dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)[c] for c in R ]
    i = sum( w )
    for p in range( len(w)-1 ):
        if w[p] < w[p+1]:
            i -= 2*w[p]
    return i
 
def int2Roman( i ):
    n, i = divmod( i, 1000 )
    R = n*'M'
    for n in [ 2, 1, 0 ]:
        w = '.0.00.000.01.1.10.100.1000.02'.split('.')[i/10**n % 10]
        R += ''.join( 'IVXLCDM'[ int(p)+2*n ] for p in w )
    return R
 
CharsSaved=0
for line in file('roman.txt'):
    old = line.strip()
    new = int2Roman( Roman2int( old ) )
    CharsSaved += len(old)-len(new)
 
print 'Characters saved:', CharsSaved
print
print time()-st