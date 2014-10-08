import string
import urllib2
x = urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
lines = string.split(x,  '\n')
numlines = 2
while lines:
     chunk = lines[:numlines]
     lines = lines[numlines:]
     for line in chunk:  print line
     if lines and raw_input('Mas?') not in ['Y', 'y']: break