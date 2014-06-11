#/usr/bin/env python
#encoding:utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 21579
BUFSIZ =1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
'''
#改进前，当client结束时，server端while循环还在，不能退出server socket，使得Port一直被占用
while True:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from :' , addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s' % (ctime(),data))

tcpCliSock.close()
tcpSerSock.close()
'''

#改进后，用try-except 捕获结束符（客户端没有发任何消息）
try:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from :' , addr
except EOFError, e:
	tcpCliSock.close()
	tcpSerSock.close()
else:
	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s' % (ctime(),data))






