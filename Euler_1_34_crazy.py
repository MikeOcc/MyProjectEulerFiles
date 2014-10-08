zzz=[int(reduce(lambda x, y: int(x) + int(y), [str(reduce(lambda x, y: x * y, range(1, int(i) + 1) + [1])) for i in str(j)])) for j in range(0, 100000) if (j == int(reduce(lambda x, y: int(x) + int(y), [str(reduce(lambda x, y: x * y, range(1, int(i) + 1) + [1])) for i in str(j)])))]


print zzz