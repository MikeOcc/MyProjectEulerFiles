#
#
#  python program for forks
#
import time
import os
global sttime
sttime=time.time()

parm = 1.1
while 1:
  parm = parm *parm
  pid = os.fork()
  if pid ==0:
    os.execlp('python','python','child.py',str(parm))
    assert 0, 'error starting program'
  else:
    print 'child is',pid
    if raw_input() == 'q':  break
