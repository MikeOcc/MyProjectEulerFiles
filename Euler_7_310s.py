from math import sqrt
#from kdecs import timing
 
def mex(s):
    
    i=0
    while i in s:
        i += 1
    return i
 
def get_nim(mx):
    nim = [0]*(mx+1)
    sq = [x**2 for x in xrange(1, int(sqrt(mx))+1)]
    #print "sq",sq
    #print
    for p in xrange(1, mx+1):
        #print p,"############"
        grundy = set()
        for s in sq :
            if p-s<0: break
            grundy.add(nim[p-s])
            #print p, s, p-s, grundy
        nim[p] = mex(grundy)
        #print "grundy",p, grundy, mex(grundy)
        #print
    return nim
 
#@timing
def p310():
    s, mx = 0, 10**5
    nim = get_nim(mx)
    nk = {k:nim.count(k) for k in set(nim)}
    #print nk
    nim_keys = sorted(nk)
    
    for a in nim_keys:
        for b in nim_keys:
            c = a^b
            if not c in nim_keys:
                continue
            if a<b<c:
                s += nk[a]*nk[b]*nk[c]
            elif a==b and b<c:
                s += (nk[a]*(nk[a]+1)*nk[c])//2
            elif a<b and b==c:
                s += nk[a]*nk[b]*(nk[b]+1)//2
            elif a==b==c:
                s += nk[a]*(nk[a]+1)*(nk[a]+2)//6
    print 'Solution: {}'.format(s)
from time import time
st = time()
p310()
print "process time", time()-st