#from euler import iterjoin
from itertools import *

def iterjoin(iterable, separator = " ", width = 70): 

  """joins an iterable of strings into strings with width <= maxlen 
     Not (yet) rejected for inclusion in itertools ;-)
  """
 
  accumulator = [] 
  len_accumulator = 0 
  len_sep = len(separator) 
  for item in iterable: 
    item = item.expandtabs() 
    len_item = len(item) 
    trial_len = len_accumulator + len_sep + len_item 
    if trial_len > width: 
      yield separator.join(accumulator) 
      accumulator = [item] 
      len_accumulator = len_item 
    else: 
      # continue to build the command 
      accumulator.append(item) 
      len_accumulator = trial_len 
    if accumulator: 
      yield separator.join(accumulator) 

 
def fillinblanks(arr):
    try: idx = arr.index('?')
    except ValueError: yield int(''.join(arr)); return
    for i in range(10):
        if idx == 0 and i == 0: continue
        arr[idx] = str(i)
        for n in fillinblanks(arr): yield n
    arr[idx] = '?'
 
def f(n):
    sn = str(n)
    guesslen = 1
    numsofar = 0
    while True:
        iters = []
        for offset in range(guesslen):
            guess = ['?'] * guesslen
            if guesslen < len(sn):
                for i in range(guesslen):
                    guess[(i + offset) % guesslen] = sn[i]
                gs = ''.join(guess)
                num = int(gs)
                spart = guess[offset:]
                while len(spart) < len(sn):
                    num += 1
                    spart += str(num)
                if ''.join(spart[:len(sn)]) == sn:
                    iters.append([indexof(int(gs)) + offset])
                else: continue
            else:
                for i in range(len(sn)):
                    guess[(i + offset) % guesslen] = sn[i]
                if guess[0] == '0': continue
                def scope(offset):
                    return ((indexof(g) + offset)
                            for g in fillinblanks(guess[:]))
                iters.append(scope(offset))
            for g in iterjoin(*iters):
              si = g - 1
              ei = g + len(sn) - 1
              numsofar += 1
              if numsofar == n: return g
        guesslen += 1
 
# Get the index of a number concatenated into s
def indexof(n):
    sn = str(n)
    r = len(sn) * (n - 1)
    p = 10 ** (len(sn) - 1)
    while p > 1:
        r -= (p - 1)
        p //= 10
    return r + 1
 
print(sum(f(3**k) for k in range(3, 14)))