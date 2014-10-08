#
#
#  Euler Problem 141
#
#
from Functions import RetFact, gcd

def p141():
    L = []
    s, limita, limitm = 0, 10**4, 10**12
    for a in xrange(2,limita):
        for b in xrange(1,a):
            if (a**3)*b+(b**2)>=limitm:
                break
            if gcd(a,b)>1:
                continue
            c=1
            while True:
                m2=(c**2)*(a**3)*b+c*(b**2)
                if m2>limitm:
                    break
                else:
                    if m2**.5==int(m2**.5):
                        s+=m2
                        L.append(m2)
                       
                c+=1
    print 'Solution: {}'.format(s)

    L=sorted(L)
    for m2 in L:
      print m2, RetFact(m2)

p141()
  
     





