#!/usr/bin/env python
#encoding:utf-8

'''
#3-4
'this is a test module'
import os
import sys

debug = True
class Fooclass(object):
	"""Foo class"""
	pass
def test():
	"""test function"""
	foo = Fooclass()
	if debug:
		print 'ran test()'

if __name__ == '__main__':
	test()


'''

'''
#3-6 第一个Python程序
"""提醒用户输入一个不存在的文件名，然后由用户输入该文件的每一行。最后将所有文本写入文本文件"""

import os
ls = os.linesep #表示一个‘\n’

#判断文件是否已经存在
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

'''
"""读取一个文件"""
fname = raw_input('Enter file name:')
print 

try:
	fobj = open(fname,'r')
except IOError, e:	
	print "*** file open error"	,e
else:
	for eachline in fobj:
		print eachline
	fobj.close()
