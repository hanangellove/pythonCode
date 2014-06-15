#/usr/bin/env python
#encoding:utf-8
'''使用threading:创建一个更加通用的模块myThread,'''

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
	
	def getResult(self):
		return self.res 

	def run(self):
		print 'starting',self.name , 'at:',ctime()
		self.res = apply(self.func,self.arg)
		print self.name,'finished at:',ctime()
		
