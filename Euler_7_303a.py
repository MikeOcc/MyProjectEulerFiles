import heapq
 
LIMIT = 100
print "b******" 
mult_digit = {}
for i in range(10):
    mult_digit[i] = {}
    for j in range(10):
        if (i * j) % 10 not in mult_digit[i]:
            mult_digit[i][(i * j) % 10] = []
        mult_digit[i][(i * j) % 10].append(j)

print "m)",mult_digit
 
def find_mult(i):
    print "c******"
    str_i = str(i)
    heap = []
    for r in range(3):
        z=mult_digit[int(str_i[-1])].get(r, [])
        print "i,z;",i,z
        heap.extend((2, [j], i * j) for j in z)
        print "!",i,j,heap
    heapq.heapify(heap)
    print "heap",heap
    used_set = set()
    while True:
        next_affected, list_n, parcial_mult = heapq.heappop(heap)
 
        if list_n[0] != 0 and max(str(parcial_mult)) < '3':
            answ=int(''.join(map(str, list_n)))
            print "answ",i,list_n,answ,answ*i
            return answ
 
        if tuple(list_n[:len(str_i)+1]) in used_set:
            continue
        used_set.add(tuple(list_n[:len(str_i)+1]))
 
        str_parcial_mult = str(parcial_mult)
        try:
            s = int(str_parcial_mult[-next_affected])
        except IndexError:
            s = 0
        for d in range(3):
            d -= s
            d %= 10
            for mult in mult_digit[int(str_i[-1])].get(d, []):
                new_list_n = [mult] + list_n
                heapq.heappush(heap, (next_affected + 1, new_list_n, parcial_mult + mult * i * (10 ** (next_affected - 1))))
 
if __name__ == '__main__':
    print "a******"
    result = 0
    #result = sum(find_mult(i) for i in range(1, LIMIT + 1))
    for i in xrange(1, LIMIT + 1):
      z = find_mult(i)
      print i,z
      result +=z

    print("The result is:", result)



