#!/usr/bin/env python
#encoding:utf-8
#3-12
import os


def makeFile():
	"""提醒用户输入一个不存在的文件名，然后由用户输入该文件的每一行。最后将所有文本写入文本文件"""
	ls = os.linesep #表示一个‘\n’

	#get file name 
	while True:
		fname = raw_input('Enter a file name:')
	
		if os.path.exists(fname):		
			print "ERROR:'%s' already exists "  %  fname
		else:
			break

	all = []
	print "\n Enter lines('.' by itself to quit).\n"

	#loop until user terminates input
	while True:
		entry = raw_input('>')
		if entry=='.':
			break
		else:
			all.append(entry)

	#write lines to file with proper line-ending
	fobj = open(fname,'w')
	fobj.writelines(['%s%s' % (x,ls) for x in all])
	fpath = fobj.tell()
	print fpath
	fobj.close()
	print 'DONE!'
	print 


def readFile():
	"""读取一个文件 readTextFile.py"""
	#get file name
	fname = raw_input('Enter file name:')
	print 

	#attempt to open file for reading
	try:
		fobj = open(fname,'r')
	except IOError, e:	
		print "*** file open error :",e
	else:
		#display contents to the screen
		for eachline in fobj:
			print eachline,
		fobj.close()
	print 

def makeOrRead():
	while True:
		print """please select your command:
				1) makeFile, -w
				2) readFile, -r
				3) quit, -q
				"""
		key = raw_input('which: ')
		if key == 'w':
			makeFile()
		elif key == 'r':
			readFile()
		elif key == 'q':
			quit()
		else:
			print 'check your input and repeat\n'

		print "********End***********\nDo you want to continue...y/n",
		result = raw_input()
		if result == 'n':
			quit()
		else:
			pass

if __name__ == '__main__':
		makeOrRead()	