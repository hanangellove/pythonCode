#/usr/bin/env python
#encoding:utf-8
'''使用线程'''

import thread
from time import ctime,sleep

def loop0():
	print 'start loop0 at :' ,ctime()
	sleep(4)
	print 'loop0 done! at :' , ctime()

print ' '

def loop1():
	print 'start loop1 at :',ctime()
	sleep(2)
	print 'loop1 done! at :',ctime()

def main():
	print 'FUNCTION start at :', ctime()
	thread.start_new_thread(loop0,()) #注意这里使用的是函数名，而不是loop0()
	thread.start_new_thread(loop1,())
	sleep(6)
	print 'all DONE at :',ctime()

if __name__ == '__main__':
	main()