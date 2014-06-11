#/usr/bin/env python
#encoding:utf-8

from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 30001
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
	"""docstring for MyRequestHandler"""
	def handle(self):
		print '...connected from :',self.client_address
		self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))

tcpServ = TCP(ADDR,MyRequestHandler)
print 'waiting fro connection...'

tcpServ.serve_forever()


		