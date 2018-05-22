#! /usr/bin/python3.5

from itertools import permutations
import sys

letters = sys.argv[1].split(',')
opFileName = str(sys.argv[2])

myfile = open( opFileName, 'w')
perm = permutations(letters, 3)

for i in list(perm):
	str = ""
	for c in i:
		str += c
	myfile.write(str + "\n")

myfile.close()
