#
#
#  python program for forks
#
import time
import os
global sttime
sttime=time.time()

def counter(count):
  for i in range(count):
     time.sleep(5)
     print '[%s] => %s' % (os.getpid(), i)

for i in range(10):
  pid = os.fork()
  if pid !=0:
    print 'Process %d spawned' % pid
  else:
    counter(10)
    os._exit(0)

print 'main process exiting.'
