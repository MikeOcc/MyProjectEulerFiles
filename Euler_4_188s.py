#
# Problem 188
#
#
global basex

basex=1777

def p(x,m):
    n,i=x,1
    while n!=1:
        i+=1
        n=(n*x)%m
        print "i,n:",i,n
    return i

L=[10**8]
print "L:",L

while L[-1]>2:
    xx=p(basex,L[-1])
    print "XX,L:",xx,L[-1]
    L.append(xx)

z=1
print "*****"
while L:
    print "b,z,m",basex,z,L
    z=pow(basex,z,L.pop())
print z


