#
#
#  Euler 213
#

import math, functools, operator
 
def pp(x, y):
    p = [[0 for j in range(30)] for i in range(30)]
    p[x][y] = 1
    for n in range(50):
        q = [[0 for j in range(30)] for i in range(30)]
        for i in range(30):
            for j in range(30):
                k = sum(1 for di,dj in ((-1,0),(1,0),(0,-1),(0,1))
                        if 0 <= i + di < 30 and 0 <= j + dj < 30)
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    if 0 <= i + di < 30 and 0 <= j + dj < 30:
                        q[i+di][j+dj] += p[i][j] / k
        p = q
    return p
 
p = [[pp(x, y) for y in range(30)] for x in range(30)]
 
print(format(sum(functools.reduce(operator.mul,
                                  (1 - p[x][y][i][j]
                                   for x in range(30) for y in range(30)), 1)
                 for i in range(30) for j in range(30)), '.9'))






