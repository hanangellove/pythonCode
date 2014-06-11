#/usr/bin/env python
#encoding:utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 21594
BUFSIZ =1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)
'''
while True:
	print 'waiting for message...'
	data,addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s' %(ctime,data),addr)
	print '...received from and returned to :',addr

udpSerSock.close()
'''

try:
	print 'UDP Transmission.'
except EOFError, e:
	udpSerSock.close()
else:
	while True:
		print 'waiting for message...'
		data,addr = udpSerSock.recvfrom(BUFSIZ)

		udpSerSock.sendto('[%s] %s' %(ctime(),data),addr)
		print '...received from and returned to :',addr

