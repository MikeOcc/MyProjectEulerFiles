x = y = 0
for i in range(500):
    y = (1 + 0.002 * i * y)/(0.5 + i * 0.001)
    x = (1 + 0.002 * i * x + 0.001 * y)/(0.5 + i * 0.001)
    print i,y,x
print "%.8f"%x


