import string
import os

xx = os.__doc__

def more(text, numlines=10):
       lines = string.split(text,  '\n')
       while lines:
               chunk = lines[:numlines]
               lines = lines[numlines:]
               for line in chunk:  print line
               if lines and raw_input('Mas?') not in ['Y', 'y']:
                    print 'zzzz' 
                    break

if __name__ ==  '__main__':
     import sys
     more(open(sys.argv[1]).read(), 10)
     print 'ZZ'
     #more(os.__doc__, 10)
