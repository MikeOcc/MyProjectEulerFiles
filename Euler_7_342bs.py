
from Functions import RofPrimes
from math import *

global p_list


def BT(p_list, max_n, p_idx, phi):
    print max_n,p_idx,phi
    res = 0
    zz = phi**(1/3.)
    if int(round(zz,4))**3==phi:  #root(phi, 3)[1]:
        # phi is cube
        res += 1
    for i in xrange(p_idx):
        p = p_list[i]
        pp = p*p
        max_n_new = max_n / p
        phi_new = phi * p * (p-1)
        mul = p
        print "maxnew",max_n_new
        while max_n_new > 0:
            print "*"
            res += mul*BT(p_list, max_n_new, i, phi_new)
            max_n_new /= p
            phi_new *= pp
            mul *= p
    return res
 
def p342(max_n = 10**10):
    res = 0
    max_n -= 1 # max_n can be reached.
    p_list = RofPrimes(2,int(sqrt(max_n))) #primes(sqrt(max_n))
    #print p_list
    #p_list=""
    #exit()
    for i, p in enumerate(p_list):
        print "!",i,p
        pp = p*p
        ppp = pp*p
        p6 = ppp*ppp
        max_n_new = max_n / pp
        phi = ppp * (p-1)
        mul = pp
        while max_n_new > 0:
            res += mul*BT(p_list, max_n_new, i, phi)
            max_n_new /= ppp
            phi *= p6
            mul *= ppp
    return res

print p342()