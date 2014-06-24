#/usr/bin/env python
#encoding:utf-8

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
dirname = 'pub/mozilla.org/data/'
#FILE = 'bugzilla-4.4.3-to-4.4.4.diff.gz'
FILE = 'PerformanceAndFootprints.html'
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
		f.cwd(dirname)#把当前工作目录设置为path
		s = f.pwd()#得到当前工作目录
		print '当前工作目录是：',s
		print f.dir(s)#显示当前工作目录的内容
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
		os.unlink(FILE)#在代码中，如果由于某些原因我们无法保存这个文件，那么要把存在的空文件删掉，乙方搞乱文件系统
	else:
		print "*** Download '%s' to CWD" % FILE
		f.quit()
		return

if __name__ == '__main__':
	main()
