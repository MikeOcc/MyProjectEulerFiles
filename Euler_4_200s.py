def gen_ab(f):
    plist = [1];
    pval = [f(2,3)];
    nval = f(3,5);
 
    while True:
        mn=-1; mnv=-1;
        for i,v in enumerate(pval):
            if(v>0 and (mn<0 or v<mnv)): mn=i; mnv=v;
        if(mn<0): break;
 
        yield mnv;
        plist[mn]+=1;
        if(plist[mn]>=len(primes)): yield -1;
        else: pval[mn]=mnv=f(primes[mn],primes[plist[mn]]);
 
        if(mnv>nval):
            np = len(plist);
            plist += [np+1];
            pval += [f(primes[np],primes[np+1])];
            nval = f(primes[np+1],primes[np+2]);
 
def gen_pairs():
    g1 = gen_ab(lambda a,b: a**3*b**2);
    g2 = gen_ab(lambda a,b: a**2*b**3);
 
    a=g1.next(); b=g2.next();
    while True:
        if(a<0 or b<0): return;
        if(a<b): yield a; a=g1.next();
        else:    yield b; b=g2.next();
 
#=====================================
 
def is_primeproof(st):
    for i in range(len(st)):
        for d in range(10):
            stn = st[:i] + str(d) + st[i+1:];
            if(is_prime(int(stn))): return False;
    return True;
 
#=====================================
 
from time import time;
from numbthy import powmod;
 
start=time();
print "Generating prime sieve";
primes = getprimes(200000);
print "Done! (%d)"%len(primes);
 
pp=0;
for x in gen_pairs():
    st=str(x);
    if(st.find("200")<0): continue;
    if not is_primeproof(st): continue;
    pp+=1;
    if(pp>=200): break;
 
print "200'th answer: %d"%x;
print "Time taken: %fms"%((time()-start)*1000);