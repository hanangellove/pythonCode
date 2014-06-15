#/usr/bin/env python
#encoding:utf-8
'''使用threading:创建一个Thread的实例，传给它一个函数'''

import threading
from time import ctime,sleep

loops = [4,2,3]

def loop(nloop,nsec):
	print 'start loop',nloop,'at :',ctime()
	sleep(nsec)
	print 'loop',nloop,'done! at :',ctime()


def main():
	
	print 'MAIN thread start at :',ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:#create a instance for Thread class
		t = threading.Thread(target=loop,args=(i,loops[i]))
		threads.append(t)

	for i  in nloops:#start threads
		threads[i].start()

	for i in nloops:#wait for all threads finish
		threads[i].join()
		
	print 'all threads Done! at :',ctime()

if __name__ == '__main__':
	main()