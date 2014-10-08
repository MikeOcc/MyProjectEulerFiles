#
#
#  python program for forks
#
import time
import os
global sttime
sttime=time.time()

import thread

def child(tid):
  print 'Hello from thread',tid

def parent():
   i = 0
   while 1:
     i +=1
     thread.start_new(child,(i,))
     if raw_input() == 'q':break


parent()
