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
#3-6 第一个Python程序 makeTextFile.py
"""提醒用户输入一个不存在的文件名，然后由用户输入该文件的每一行。最后将所有文本写入文本文件"""

import os
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
'''

'''
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
		print eachline
	fobj.close()
'''

#练习题：
'''
3-1.    标识符。为什么 Python 中不需要变量名和变量类型声明?

答：因为变量在第一次赋值的时候就被自动声明了。

 

3–2.   标识符。为什么 Python 中不需要声明函数类型?

答：我想和变量一样，是动态类型，    在创建--也就是赋值时,解释器会根据语法和右侧的操作数来决定新对象的类型。
在对象创建后,一个该对象的应用会被赋值给左侧的变量。

3–3.   标识符。为什么应当避免在变量名的开始和和结尾使用双下划线?

答：因为这在python中是专用的，__xxx__表示系统定义的名字


3–4.   语句。在 Python 中一行可以书写多个语句吗?

Ans:OK。用“;”
3–5. 语句。在 Python 中可以将一个语句分成多行书写吗?

Ans:OK,using "/"
'''


#3-10 使用异常处理替换os.path.exists()
'''
#3-6 第一个Python程序 makeTextFile.py
"""提醒用户输入一个不存在的文件名，然后由用户输入该文件的每一行。最后将所有文本写入文本文件"""

import os
ls = os.linesep #表示一个‘\n’

#get filename 
fname = raw_input('Enter a file name:')

all = []
print "\n Enter lines('.' by itself to quit).\n"

#loop until user terminates input
while True:
	entry = raw_input('>')
	if entry=='.':
		break
	else:
		all.append(entry)

#write lines to file with proper line-ending --use exception handling
try:
	fobj = open(fname,'w')
except IOError, e:
	print 'file open error:',e
else:
	fobj.writelines(['%s%s' % (x,ls) for x in all])
	fpath = fobj.tell()
	print fpath
	fobj.close()
	print 'DONE!'
'''

#3-11
'''
#readTextFile.py
import os

#get file name
fname = raw_input('Enter file name:')
print 
isFileExist = True
#attempt to open file for reading
if not os.path.exists(fname):
	print "文件不存在！"
	isFileExist = False

if isFileExist :
	#display contents to the screen
	fobj = open(fname,'r')
	for eachline in fobj:
		print eachline, #print (str(eachline).strip())--//print eachline.strip()--strip()方法先删除字符串两端的空白，在利用print自动生成newline。
		
	fobj.close()

'''
#3-12
makeAndReadFile.py
#3-13
