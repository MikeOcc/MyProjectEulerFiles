#
#
#
#


import re
words=re.findall('\w+', open('/python/OW.txt').read().lower())
print len(words)