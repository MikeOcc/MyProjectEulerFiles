from time import time

old=['JIK']
new=[]
tba='ABCDEFGH'

print tba[::-1]

t0=time()
for k in tba[::-1]:

    print k
    new=[]
    if len(old)<30: print len(old), old
    for j in old:
        for i in xrange(1,len(old[0])):
            #print "new1:",new
            new+=[j[-1:-i-1:-1]+k+j[:-i]]
            #print "new2:", new
    old=new


#print old
old.sort()

for i in xrange(len(old)):
  print i,old[i]

print time()-t0,old[2010]
