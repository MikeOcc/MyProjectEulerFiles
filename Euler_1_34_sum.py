factorials = {'0' : 1, '1' : 1, '2' : 2, '3' : 6, '4' : 24, '5' : 120,
              '6' : 720, '7' : 5040, '8' : 40320, '9' : 362880}
print sum(num for num in xrange(3, 50000) if num == sum(factorials[x] for x in str(num)))



#factorials = {'0' : 1, '1' : 1, '2' : 2, '3' : 6, '4' : 24, '5' : 120,  '6' : 720, '7' : 5040, '8' : 40320, '9' : 362880}

fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
print sum(num for num in xrange(3, 50000) if num == sum(fact[int(x)] for x in str(num)))


#num=10023456765
#for x in str(num):print x,type(x)