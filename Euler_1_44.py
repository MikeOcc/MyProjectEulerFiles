#
# P(n) = (3*n**2 -n)/2
#
#Find the pair of pentagonal numbers, Pj and Pk,
#for which their sum and difference is pentagonal
# and D = |Pk  Pj| is minimised; what is the value of D?
#

pset=[]

for i in range(1,10000):

  pset.append((3*i**2 -i)/2)


pset = set(pset)

dmin =10000000000000
pj,pk = 0,0
for j in pset:
  for k in pset:
     if abs(j-k) in pset: 
       if abs(j+k) in pset:
          print j,k,abs(j-k),abs(j+k)
          if abs(j-k) < dmin:
            dmin = abs(j-k)
            pj,pk = j,k
            print "*",j,k,abs(j-k),abs(k+k),dmin

print "Pentagonal #s Pj and Pk with Dmin=|Pk-Pj| is",pj,pk,dmin

   



