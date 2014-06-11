#/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21594
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)
#udpCliSock.connect(ADDR)

while True:
	data = raw_input('>')
	if not data:
		break
	udpCliSock.sendto(data,ADDR)
	data,ADDR= udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data

udpCliSock.close()
