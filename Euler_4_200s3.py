#!/usr/bin/env python
 
from itertools import count
from Functions import IsPrime
import bisect
 
## ************************ CLASSES ***************************
 
class Merger:
    def __init__(self, gens=[]):
        self.gens = []
        for gen in gens:
            self.addGen(gen)
 
    def __iter__(self):
        return self
 
    def addGen(self, gen):
        bisect.insort(self.gens, (gen.next(), gen) )
 
    def next(self):
        (minV, gen) = self.gens.pop(0)
        self.addGen(gen)
        return (minV, gen)
 
 
class Squbes(Merger):
    def __init__(self):
        self.keyServer = primesGen()
        Merger.__init__(self)
        self.addGenKey()
 
    def addGenKey(self):
        key = self.keyServer.next()
        gen = (key**3 * p**2 for p in primesGen() if p != key)
        self.addGen(gen)
        self.lastGen = gen
 
    def next(self):
        (n, gen) = Merger.next(self)
        if gen is self.lastGen:
            self.addGenKey()
        return (n, gen)
 
## ************************ SUBROUTINES ***************************
 
def primesGen():
    return (n for n in count(2) if IsPrime(n))
 
def neighNumbers(n):
    digits = list(str(n))
    for (i, d) in enumerate(digits):
        for d2 in '0123456789':
            if (i > 0 or d2 != '0') and d2 != d:
                digits[i] = d2
                yield int(''.join(digits))
                digits[i] = d
 
def isPrimeProof(n):
    return all(not IsPrime(m) for m in neighNumbers(n))
 
## ************************ MAIN ***************************
 
counter = 0
for (n, _) in Squbes():
    if str(n).rfind('200') >= 0 and isPrimeProof(n):
        counter += 1
        if counter == 200:
            print 'Solution:', n
            break