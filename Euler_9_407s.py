from time import time

def eea(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

start = time()

N = 10**7
p = [0, 0] + [1 for n in range(N - 1)]

for p1 in range(2, N + 1):
   p2 = p1 + 1
   while p1*p2 <= N:
      d, a, b = eea(p1, p2)

      if 1 == d:
         n = p1*p2
         e1 = (n + a*p1) % n
         e2 = (n + b*p2) % n

         p[n] = max(p[n], e1, e2)
      p2 += 1

print(time() - start, sum(p))