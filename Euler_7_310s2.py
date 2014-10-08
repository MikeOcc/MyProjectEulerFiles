from math import sqrt
#from kdecs import timing
 
def mex(s):
    
    i=0
    while i in s:
        i += 1
    return i
 
def get_nim(mx):
    nim = [0]*(mx+1)
    #sq = [x**2 for x in xrange(1, int(sqrt(mx))+1)]
    #print "sq",sq
    #print
    p = 1
    while p <=mx:
        #print p,"############"
        grundy = set()
        s = 1
        while p-s**2>-1:
            grundy.add(nim[p-s**2])
            #print p, s**2, p-s**2, grundy
            s+=1
        nim[p] = mex(grundy)
        #print "grundy",p, grundy, mex(grundy)
        #print

        p+=1
    print sum(list(nim)),"!!"
    return nim
 
#@timing
def p310():
    s, mx = 0, 10**5
    nim = get_nim(mx)
    print
    #print nim
    nk = {k:nim.count(k) for k in set(nim)}
    #print nk
    nim_keys = sorted(nk)
    print "len", len(nim_keys)
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
 
p310()