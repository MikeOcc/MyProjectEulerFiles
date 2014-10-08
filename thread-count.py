#
#
#  python program for forks
#
import time
import os
global sttime
sttime=time.time()

import thread

def counter(myID,count):
    for i in range(count):
       time.sleep(1)
       print '[%s] => %s' % (myID, i)

for i in range(10):
  thread.start_new(counter, (i,100))

time.sleep(4)

print 'main thread exiting'
