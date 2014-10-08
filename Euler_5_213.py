#
#  project Euler 213
#


try: import psyco
except:pass
 
from collections import defaultdict
 
def p213():
    side = 30
    n_jumps = 50
 
    single_jump = ((0, 1), (0, -1), (-1, 0), (1, 0))
    next_matrix = {}
    for y in xrange(side):
        for x in xrange(side):
            tot = 0
            where = defaultdict(int)
            for dx, dy in single_jump :
                if 0 <= x + dx < side and 0 <= y + dy < side:
                    where[(x+dx, y+dy)] += 1
            next_matrix[(x, y)] = (len(where), where)
 
    matrix = [[{x+(y*side):1.0} for x in xrange(side)] for y in xrange(side)]
    for n_jump in xrange(n_jumps):
        new_matrix = [[defaultdict(float) for x in xrange(side)] for y in xrange(side)]
        for x in xrange(side):
            for y in xrange(side):
                for flea in matrix[x][y]:
                    for nx, ny in next_matrix[(x, y)][1]:
                        new_matrix[nx][ny][flea] += matrix[x][y][flea]*(1.0/next_matrix[(x, y)][0])
        matrix = new_matrix
 
    empty_expected = 0.0
    for x in xrange(side):
        for y in xrange(side):
            empty_expected += reduce(float.__mul__, (1 - p for p in matrix[x][y].values()))
    print empty_expected
 
try: psyco.full()
except: pass
p213()




