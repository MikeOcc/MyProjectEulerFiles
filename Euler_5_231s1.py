def fill_factors(mn,mx):
    total=0;
    for p in primes:
        for e in xrange(1,30):
            pe=p**e;
            if(pe>mx): break;
            for i in xrange((mn/pe)*pe,mx+1,pe):
                if(i<mn): continue;
                total+=p;
    return total;

#=========================================

from globals import getprimes;
from time import time;
import psyco;

psyco.full();

start=time();
n,r=20000000,15000000;
primes = getprimes(n);
total=fill_factors(r+1,n)-fill_factors(2,n-r);

print "Total: %d"%total;
print "Time taken: %fs"%(time()-start);