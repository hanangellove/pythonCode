#/usr/bin/env python
#encoding:utf-8

from socket import *

HOST = ''
PORT = 30001
BUFSIZ = 1034
ADDR = (HOST,PORT)

while True:
	tcpCliSock = socket(AF_INET,SOCK_STREAM) 
	tcpCliSock.connect(ADDR)
	data = raw_input('>')
	if not data :
		break
	tcpCliSock.send('%s\r\n' % data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data.strip()

tcpCliSock.close()