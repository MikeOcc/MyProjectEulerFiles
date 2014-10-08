#
#
# Euler 301
#
#

#cnt = 0

def nim(heaps, misere=True):
        #Computes next move for Nim in a normal or misere (default) game, returns tuple (chosen_heap, nb_remove)
        global cnt
        X = reduce(lambda x,y: x^y, heaps)

        if X == 0: # Will lose unless all non-empty heaps have size one
                #print "You will lose :("
                cnt+=1
                for i, heap in enumerate(heaps):
                        if heap > 0: # Empty any (non-empty) heap
                                chosen_heap, nb_remove = i, heap
                                break
        else:
                sums = [t^X < t for t in heaps]
                chosen_heap = sums.index(True)
                nb_remove = heaps[chosen_heap] - (heaps[chosen_heap]^X)
                heaps_twomore = 0
                for i, heap in enumerate(heaps):
                        n = heap-nb_remove if chosen_heap == i else heap
                        if n>1: heaps_twomore += 1
                # If move leaves no heap of size 2 or larger, leave an even (misere) or odd (normal) number of heaps of size 1
                if heaps_twomore == 0: 
                        chosen_heap = heaps.index(max(heaps))
                        heaps_one = sum(t==1 for t in heaps)
                        # misere (resp. normal) strategy: if it is even (resp. odd) make it odd (resp. even), else do not change
                        nb_remove = heaps[chosen_heap]-1 if heaps_one%2!=misere else heaps[chosen_heap]
        return chosen_heap, nb_remove


def X(a,b,c):

  return a^b^c

n=7
cnt = 0
for i in xrange(1,2**n+1):
   cnt+=(X(i,i*2,i*3)==0)
 
  #Heap=(i,2*i,3*i)

  #result = nim(Heap,False)
  #print result  

#print "answer for n =",(n,2**n)," is", cnt, 2**n-cnt
print "answer for n =",(n,2**n)," is", cnt, 2**n-cnt



