#!/usr/bin/env python3

import csv
import sys

sitesOfInterest = {19, 33, 120, 311}

with open('table3_subs_edit.csv') as csvfile:
	aaReader = csv.reader(csvfile)
	lineNumber = 0
	for row in aaReader:
		lineNumber +=1
		nonEmptyFields = [] #made a list of non empty fields
		for field in row:
			field = field.strip() # remove emty spaces end or start
			field = field.replace('del', '-') #del at the start of sequences were causing issues, because middle fields could be converted to intergers
			if field != '':
				nonEmptyFields.append(field) #

		nFields = len(nonEmptyFields)
		if nFields < 2: #testing that the data looks good
			print('Found a line without at least 2 fields.')
			sys.exit(1)

		if row[0] == row[1] and nFields != 2: #if there are two fields and they are the same, it doesnt matter that much, just duplicated
			print('On line %d, both ids are %s but there are no'
			'mutations.' % (lineNumber, row[0]),
			file=sys.stderr)
			# sys.exit(1)- dont exit
		else:
			print('On line %d, both ids are %s but there are %d'
			'extra fields.' % (lineNumber, row[0], nFields -2, ','.join(row[2:]))) 
			#divide in commas, then join them, and give us everything ahead of field 2
			sys.exit(1)

		#seq1 = nonEmptyFields[0]
		#seq2 = nonEmptyFields[1]

		# or use pop, removes the last thing last thing

		seq1 = nonEmptyFields.pop(0)
		seq1 = nonEmptyFields.pop(0)


		for field in nonEmptyFields:
			if len(field) < 3:
				print('On line %d, there is too short field %s' % (lineNumber, field),
					file=sys.stderr)
			aa1 = field[0]
			aa2 = field [-1]
			try: #try to do something, if not give error
				location = int(field[1:-1]) #makes a string into an interger, if it's a character it'll give error
			except ValueError:
				print('On line % there is an unparseable field %r.'
					% (lineNumber, field), file=sys.stderr)

#### actual command that does the job
			if site in sitesOfInterest:
				print('%s vs %s: Change from %s to %s at site %d'
					% (seq1, seq2, aa1, aa2, site))






