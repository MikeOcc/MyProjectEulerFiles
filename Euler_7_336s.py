from time import time

old=['JIK']
new=[]
tba='ABCDEFGH'

t0=time()
for k in tba[::-1]:
    new=[]
    if len(old)<30: print len(old), old
    for j in old:
        for i in xrange(1,len(old[0])):
            new+=[j[-1:-i-1:-1]+k+j[:-i]]
    old=new

old.sort()

print time()-t0,old[2010]
