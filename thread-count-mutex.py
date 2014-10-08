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
       mutex.acquire()
       time.sleep(1)
       print '[%s] => %s' % (myID, i)
       mutex.release()

mutex = thread.allocate_lock()
for i in range(10):
  thread.start_new(counter, (i,3))

time.sleep(10)

print 'main thread exiting'
