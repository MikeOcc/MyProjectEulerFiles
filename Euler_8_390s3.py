from time import time

def isqrt(n, guess=1):
 xn = xn1 = guess
 xn1 += (n/xn - xn)/2
 while xn != xn1:
  xn = xn1
  xn1 += (n/xn - xn)/2
 return xn1


def ta(i, j):
 # based on heron's formula
 # simplifed using i/2 and j/2
 # as uneven i and j are not possible
 x = i+j
 y = 2*i*j
 area = isqrt(x*x + y*y - y, y + i)
 if area<max_e1: return area
 return 0


# main sequence
# (2, 8), (2, 144), (2, 2584), ...
# (4, 32), (4, 2112), (4, 139360), ...
# (6, 72), (6, 10512), (6, 1534680), ...
# ...
def type1set(i):
 i_e2 = i*i
 lim = max_2 / i
 #lim = ((max_e2 - i_e2)/(4*i_e2 + 1))**0.5
 t = 0
 s = 4*i_e2
 d = 16*i_e2 + 2
 r = [0]
 x = 0
 while s<lim:
  t += ta(i, s)
  t += type2set(s, i, r[x])
  r += [s]
  s = r[x+1]*d - r[x]
  x += 1
 return t


# extended sequences
# numbers which have been previously generated exist in multiple sequences
def type2set(i, c, m):
 i_e2 = i*i
 lim = max_2 / i
 #lim = ((max_e2 - i_e2)/(4*i_e2 + 1))**0.5
 t = 0
 ratio = (i - m) / c
 s = ratio * i - c
 d = 16*i_e2 + 2
 r = [-s, -c, c]
 x = 0
 while s<lim:
  t += ta(i, s)
  t += type2set(s, i, r[x+1])
  r += [s]
  s = r[x+2]*d - r[x]
  x += 1
 return t


def test(exp):
 global max_e1, max_e2, max_2

 max_e1 = int(10**exp)
 max_e2 = int(100**exp)
 max_2 = max_e1 / 2

 t = 0
 i_max = int(max_e1**(1.0/3.0)/2)
 for i in range(1, i_max + 1):
  t += type1set(i)
 return t

for i in range(10, 21):
 start = time()
 print i, test(i), `time() - start` + 's'