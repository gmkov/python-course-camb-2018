# cat NEO*q| egrep '^[ACGT]+$' | awk 'length > 50 '| cut -c1-20 | sort | uniq -c | sort -n -r 

import sys #import for system preferences
import re #import for regular expression

# make regular expression and compile it before the program
# so that then it can just be called
# regular expression language similar across languages

patternacgt = re.compile('^[ACGT]+$')

#collect preffixes in an array
prefixes = []

for line in sys.stdin:
	if len(line) > 50 and patternacgt.match(line):
		prefixes.append(line[0:30])

prefixes.sort()

for prefix in prefixes:
	print(prefixes)





