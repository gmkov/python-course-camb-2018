import sys
for bananas in sys.stdin:
	print(bananas)

# equivalent
from sys import stdin
for bananas in stdin:
	print(bananas)

# now make pro
import sys
seen = set()
for bananas in sys.stdin:
	if bananas.startswith('>'):
		if bananas in seen:
			print('Hey, I already saw that one', bananas)

