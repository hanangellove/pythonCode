#/usr/bin/env python
#encoding:utf-8
'''创建一个能接收客户的消息，在消息钱加一个时间戳后返回的TCP服务器'''
from socket import *
import os

HOST = ''
PORT = 50002
BUFSIZ =1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    print 'waiting for connection...'
    tcpCltSock, addr = tcpSerSock.accept()
    print '...connected from :' , addr
except EOFError, e:
    tcpCltSock.close()
    tcpSerSock.close()
else:
    while True:
        data = tcpCltSock.recv(BUFSIZ)
        if not data:
            break
        print 'recieved command from :',addr,data
        cmdResult =  os.popen(data).read()
        tcpCltSock.sendall(cmdResult)
