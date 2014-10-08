from time import time
st=time()


from itertools import combinations

cubenums=[0,1,2,3,4,5,6,7,8,9]



x1 = combinations(cubenums,6)
x3 = combinations(cubenums,6)


cublist, c2=[],[]

for zzz in x3:
  cublist.append(zzz)


for zzz in x1:
  c2.append(zzz)

"""
print x1
print
for yy in x2:
  print yy
"""
a,b,c,d,e,f,g,h,i=False,False,False,False,False,False,False,False,False
summ=0
ctr=0
for z2 in cublist:
  print "****"
  for z in c2:
    a,b,c,d,e,f,g,h,i=False,False,False,False,False,False,False,False,False
    ctr+=1
    print ctr,z,z2

    if set(z).union(set(z2)) != set(cubenums):continue

    if (0 in z and 1 in z2) or (1 in z and 0 in z2):a=True

    if (0 in z and 4 in z2) or   (4 in z and 0 in z2):b=True

    if (0 in z and 9 in z2) or     (9 in z and 0 in z2):c=True

    if (6 in z and 1 in z2) or     (1 in z and 6 in z2):d=True

    if (2 in z and 5 in z2) or     (5 in z and 2 in z2):e=True

    if (3 in z and 6 in z2) or     (6 in z and 3 in z2):f=True

    if (4 in z and 6 in z2) or     (6 in z and 4 in z2):g=True

    if (4 in z and 9 in z2) or     (9 in z and 4 in z2):g=True

    if (1 in z and 8 in z2) or     (8 in z and 1 in z2):h=True

    if a and b and c and d and e and f and g and h:summ+=1

print "number of combos is", summ


print "Process time is", time()-st