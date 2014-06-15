#/usr/bin/env python
'''普通两个顺序执行的函数'''
from time import ctime,sleep

def loop0():
	print 'start loop0 at :' ,ctime()
	sleep(4)
	print 'loop0 done!'

def loop1():
	print 'start loop1 at :',ctime()
	sleep(2)
	print 'loop1 done!'

def main():
	print 'start at :', ctime()
	loop0()
	loop1()
	print 'all DONE at :',ctime()

if __name__ == '__main__':
	main()