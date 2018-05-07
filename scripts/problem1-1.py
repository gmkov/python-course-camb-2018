# now make programme that prints pretty duplicated names
import sys
seen = set() # list of unique values
for inputLine in sys.stdin:
	if inputLine.startswith('>'):
		fastaId = inputLine[1:]
		if fastaId in seen:
			print('Hey, I already saw that one', fastaId)
			sys.exit()
		seen.add(fastaId) # add this so that it prints the right sample name

