#/usr/bin/env python
#encoding:utf-8

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
dirname = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-4.4.3-to-4.4.4.diff.gz'

def main():
	#创建ftplib连接
	try:
		f = ftplib.FTP(HOST)
	except (socket.error,socket.gaierror), e:
		print "ERROR:cannot reach '%s'" % HOST
		return
	print "***connected to host '%s'" % HOST

	#登录到ftplib服务器
	try:
		f.login()#不需要密码的FTP服务器就不带入参数
	except ftplib.error_perm, e:
		print "ERROR:cannot login anonymously"
		f.quit()
		return
	print "***login in as 'anonymously'"

	#进入dirname目录
	try:
		f.cwd(dirname)
	except ftplib.error_perm, e:
		print "ERROR:cannot cd to '%s'" % dirname
		f.quit()
		return
	print "***change to '%s' folder " % dirname

	#获取文件 
	try:
		
		#f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
		locfile = open(FILE,'wb').write
		f.retrbinary('RETR %s' % FILE,locfile)
	except ftplib.error_perm, e:
		print "ERROR:cannot read file '%s' " % FILE
		os.unlink(FILE)
	else:
		print "*** Download '%s' to CWD" % FILE
		f.quit()
		return

if __name__ == '__main__':
	main()
