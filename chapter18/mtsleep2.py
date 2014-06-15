#/usr/bin/env python
#encoding:utf-8
'''使用线程和锁：当子线程都执行完之后，立即结束主线程'''

import thread
from time import ctime,sleep
loops = [4,2]

def loop(nloop,nsec,lock):
	print 'start loop',nloop,' at :' ,ctime()
	sleep(nsec)
	print 'loop',nloop,' done! at :' , ctime()
	lock.release()


def main():
	print 'FUNCTION start at :', ctime()

	locks = []
	nloops = range(len(loops))

	for i in nloops:
		lock = thread.allocate_lock()
		lock.acquire()
		locks.append(lock)#元组中的append方法，添加对象到元组中

	for i in nloops:
		thread.start_new_thread(loop,(i,loops[i],locks[i]))
		#thread.start_new_thread(function, args)
	for i in nloops:
		while locks[i].locked():
			pass


	print 'all DONE at :',ctime()

if __name__ == '__main__':
	main()