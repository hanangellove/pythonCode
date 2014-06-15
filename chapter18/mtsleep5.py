#/usr/bin/env python
#encoding:utf-8
'''使用threading:派生一个Thread的子类，创建这个子类的实例'''

import threading
from time import ctime,sleep

loops = [4,2,3]

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, func,arg,name=''):
		super(MyThread, self).__init__()
		self.arg = arg
		self.func = func
		self.name = name
		
	def run(self):
			apply(self.func,self.arg)	

def loop(nloop,nsec):
	print 'start loop',nloop,'at :',ctime()
	sleep(nsec)
	print 'loop',nloop,'done! at :',ctime()


def main():
	
	print 'MAIN thread start at :',ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:#create a instance for Thread class
		t = MyThread(loop,(i,loops[i]))
		threads.append(t)

	for i  in nloops:#start threads
		threads[i].start()

	for i in nloops:#wait for all threads finish
		threads[i].join()
		
	print 'all threads Done! at :',ctime()

if __name__ == '__main__':
	main()