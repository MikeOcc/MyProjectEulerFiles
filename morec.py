import string
import os


def more(text, numlines=15):
       lines = string.split(text,  '\n')
       while lines:
               chunk = lines[:numlines]
               lines = lines[numlines:]
               for line in chunk:  print line
               if lines and raw_input('Mas?') not in ['Y', 'y']: break

if __name__ ==  '__main__':
     import sys
     #more(open(sys.argv[1]).read(), 10)
     x = sys.__doc__
     #x = sys.modules
     more(x, 10)
