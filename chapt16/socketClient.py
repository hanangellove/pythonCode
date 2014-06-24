#/usr/bin/env python
from socket import *

HOST = 'localhost'
PORT = 50002
BUFF = 1024
ADDR = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM)
s.connect(ADDR)

while True:
    cmd = raw_input('Enter your command:').strip()
    if not cmd:
        continue
    s.sendall(cmd)
    data = s.recv(BUFF)
    print data,
s.close()
