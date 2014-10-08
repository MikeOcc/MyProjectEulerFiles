from time import time
 
def mex(s):
    
    i=0
    while i in s:
        i += 1
    return i
###############################
st = time()
s, max = 0, 10**5

nimbers = [0]*(max+1)

p = 1
for p in xrange(1,max+1):
    #print p,"############"
    grundy = set()
    sqr = 1
    while p-sqr**2>-1:
        grundy.add(nimbers[p-sqr**2])
        sqr+=1
    nimbers[p] = mex(grundy)
    #print "grundy",p, grundy, mex(grundy)
    #print


print
#print nimbers
#print sum(list(nimbers)),"!!"

nk = {k:nimbers.count(k) for k in set(nimbers)}

#print nk

nimber_keys = sorted(nk)

print "len", len(nimber_keys)

for a in nimber_keys:
    for b in nimber_keys:
        c = a^b
        if not c in nimber_keys:
            continue
        if a<b<c:
            s += nk[a]*nk[b]*nk[c]
        elif a==b and b<c:
            s += (nk[a]*(nk[a]+1)*nk[c])//2
        elif a<b and b==c:
            s += nk[a]*nk[b]*(nk[b]+1)//2
        elif a==b==c:
            s += nk[a]*(nk[a]+1)*(nk[a]+2)//6

print "Answer is",s
print "Process time is", time()-st

 
