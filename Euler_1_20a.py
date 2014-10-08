
#lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))]

#reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])

def make_incrementor (n): return lambda x: x + n

f= make_incrementor(2)

#print f(42), f(99)

def make2 (y): return lambda x: x + y**2

h = make2(100)

#print h(2)

#print make2(100)(2)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 9 == 0 , foo)
print reduce(lambda x,y: x+7|3,  foo)

reduce(lambda x,y: x*y,  range(1,500))
