#/usr/bin/env python
#encoding:utf-8
'''使用threading:创建一个Thread的实例，传给它一个可调用的类对象'''

import threading
from time import ctime,sleep

loops = [4,2,3]
class threadFunc(object):
	"""docstring for threadFunc"""
	def __init__(self, func,args,name=''):
		self.args = args
		self.name = name
		self.func = func
	
	def __call__(self):#__call__表示可调用的实例
			apply(self.func,self.args)	

def loop(nloop,nsec):
	print 'start loop',nloop,'at :',ctime()
	sleep(nsec)
	print 'loop',nloop,'done! at :',ctime()


def main():
	
	print 'MAIN thread start at :',ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:#create a instance for Thread class
		t = threading.Thread(target=threadFunc(loop,(i,loops[i]),loop.__name__))
		threads.append(t)

	for i  in nloops:#start threads
		threads[i].start()

	for i in nloops:#wait for all threads finish
		threads[i].join()
		
	print 'all threads Done! at :',ctime()

if __name__ == '__main__':
	main()