import sys

wordCounts = {} # create empty dictionary

for inputLine in sys.stdin:
	inputLine = inputLine[:-1] # assign old variable except for the last character
	for word in inputLine.split(): # split returns a list
		for x in "',.": #knows it's a list, iteration
			word= word.replace(x, ' ')
		# word = word.replace("'", "").replace(",", "").replace(".", "")
		if word in wordCounts:
			wordCounts[word] += 1 #+= means add these things to whats before
		else:
			wordCounts[word] = 1

print(wordCounts)

# order the dictionary
# flip the key and value, to make a list that 
# one liner
# newList = [(count, word) for (word, count) in wordCounts.items()]

newList = []
for (word, count) in wordCounts.items():
	newList.append((count, word))

# now sort this list
print(sorted(newList, reverse=True)) # universal function that gives a new object

# newList.sort() would change the original list, change the object

def keyfunc(t):
	return t[1]

for word in sorted(wordCounts, reverse=True, key=keyfunc):
	print(word, wordCounts[word])


	





