#/usr/bin/env python
#encoding:utf-8
from random import randint
from time import sleep,ctime
from Queue import Queue
from myThread import MyThread

def writeQ(queue):
	print 'producing bread fro Q...',
	queue.put('bread',1)
	print 'size now',queue.qsize()
def readQ(queue,who):

	val = queue.get(1)
	if who is 'Bob':
		print 'Bob eat a bread from Q... size now',queue.qsize()
	elif who is 'Shawn':
		print 'Shawn eat a bread from Q... size now',queue.qsize()
	else:
		print 'Li eat a bread from Q... size now',queue.qsize()
	

def writer(queue,loops):
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1,3))
def reader(queue,loops):
	who = ['Bob','Shawn','Li']
	for i in range(loops):
		j = randint(0,len(who)-1)
		readQ(queue,who[j])
		sleep(randint(2,5))

funcs = [writer,reader]
nfunc = range(len(funcs))

def main():
	nloops = randint(2,5)
	print 'nloops is %s:' % nloops
	q = Queue(32)

	threads = []
	for i in nfunc:
		t = MyThread(funcs[i],(q,nloops),funcs[i].__name__)
		threads.append(t)

	for i in nfunc:
		threads[i].start()

	for i in nfunc:
		threads[i].join()

	print 'all done!'
if __name__ == '__main__':
	main()