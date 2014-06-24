#/usr/bin/env python
#encoding:utf-8

import os
'''
f = open('file1.txt','r')
for line in f :
	if line[0] == '#':
		continue
	print line,
f.close()
'''
#9-2
f = open('file1.txt','r')
N = raw_input('Enter a number:')
i = 1

for line in f :

	if i <= N:
		print line,
	i+=1
f.close()

