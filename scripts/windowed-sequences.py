#!/usr/bin/env python3
import sys #access to the command line
from Bio import SeqIO

########
# define functions the prgram will use
def analyze1(seq, windowSize):
	print('The sequence is', seq, 'the window size is', windowSize,
		'and has length', len(seq))
	start = 0
	stop = start + windowSize 
	len = len(seq)

	def countGs(s):
		return s.count('G') #define another function within function that will be used by analyze

	while stop < length: #we are going to ignore the last bit of the sequence that does not have enough reads to fill a window
		window = seq[start:stop] #cutting the piece with []
		print('   The next window is' window)
		print('   The G count is' countGs(window))
		start += windowSize
		stop += windowSize

def analyze2(seq, windowSize):
	print('fake analysis!') 

# add function that does windows, with a step
def analyze3(seq, windowSize):
	print('The sequence is', seq, 'the window size is', windowSize,
		'and has length', len(seq))
	start = 0
	stop = start + windowSize 
	len = len(seq)

	def countGs(s):
		return s.count('G') #define another function within function that will be used by analyze

	while stop < length: #we are going to ignore the last bit of the sequence that does not have enough reads to fill a window
		window = seq[start:stop] #cutting the piece with []
		print('   The next window is' window)
		print('   The G count is' countGs(window))
		start += windowSize
		stop += windowSize


########
# define arguments
parser = argparse.ArgumentParser(
	description='Script to do a window analysis')

parser.add_argument(
	'--analyzeFunction', default='analyze1', # must add a default to arguments
	choices=('analyze1', 'analyze2'),
	help='The analysis type')

parser.add_argument(
	'--windowSize', 'w', type=int, default =10, # must add a default to arguments
	help='The sliding window size')

parser.add_argument(
	'--verbose', 'v', action='store_true', default=True, # must add a default to arguments
	help='TIf given print extra helpful output')

args = parser.parse_args()

########
# what to do in case any of the options are specified (other than default)
if args.verbose:
	print("hey welcome to version 0.0.0.01 of our"
		"program....")

if args.analyzeFunction == 'analyze1':
	analyzeFunc = analyze1
else:
	analyzeFunc = analyze2

########
# analysis
for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence=str(record.seq)
    analyzeFunc(sequence, args.windowSize)







