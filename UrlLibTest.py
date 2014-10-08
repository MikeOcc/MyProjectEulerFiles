import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
         print line