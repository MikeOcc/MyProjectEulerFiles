#
#
#  python program for forks
#
from time import time
import os
global sttime
sttime=time()

def child():
  print 'Hello from child', os.getpid() , ":" ,time()-sttime
  os._exit(0)

def parent():
  #sttime = time()
  while True:
    newpid = os.fork()
    if newpid ==0:
      child()
    else:
      print 'Hello from parent', os.getpid(),newpid
    if raw_input() == 'q':
      break
    else:
      print raw_input()
parent()
