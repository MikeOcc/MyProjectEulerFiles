def main():
    fact = dict(zip(range(10),
                    (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)))
 
    cycle_distance = {}
 
    for n in xrange(1000000):
        #if n % 10000 == 0:
        #    print n
        if n in cycle_distance:
            print "found"
            continue
        print "****" ,cycle_distance
        chain = [n]
        d = n
        while 1:
            tot = 0
            while d:
                zz = fact[d % 10]  #;print d,zz
                tot += zz   #fact[d % 10]
                d //= 10
            d = tot
 
            if tot in cycle_distance:
                # Connected to something known
                offset_dist = cycle_distance[tot] + 1
                chain.reverse()
                for dist, value in enumerate(chain):
                    cycle_distance[value] = dist + offset_dist
                break
            elif tot in chain:
                # Loop to self
                for dist, value in enumerate(chain[::-1]):
                    cycle_distance[value] = dist+1
                break
            chain.append(tot)
 
    print cycle_distance.values().count(60)
 
main()