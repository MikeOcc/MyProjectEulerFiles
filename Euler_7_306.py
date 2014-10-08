#
#
#  Euler Problem 306
#
#

class memoize(object):
    '''
    newfunc = memoize(func) is a memoized version of func.
    '''
    def __init__(self, f):
        self.cache = {}
        self.f = f

    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        else:
            result = self.f(*args)
            self.cache[args] = result
            return result

import re

def moves(config):
    '''
    Return all board states which can result after making one move.
    '''
    return (config[:i] + "11" + config[i+2:] for m in re.finditer(r"00+",config) 
        for i in range(m.start(),m.end()-1))

@memoize
def wins(config):
    '''
    Return True iff the player whose turn it is can force a win.
    '''
    # Exercise for the reader that this does the correct thing
    # 1) in general
    # 2) if moves(config) is empty
    if all(wins(new_config) for new_config in moves(config)):
        return False
    return True

print [n for n in range(36) if wins("0"*n)] 




