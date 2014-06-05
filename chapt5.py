#/usr/bin/env python
#encoding:utf-8
'''
#5-3
import os

def score():
	while True:
		sco = raw_input("Enter a score :")

		if sco == 'q':
			quit()
		else:
			try:
				s = int(sco)
			except ValueError, e:
				print "Error:",e
				raw_input("please input again...") 
			else:
				if s>=90  and s<=100:
					print "A"
				elif s>=80 and s <=89:
					print "B"					
				elif s>=70 and s <=79:
					print "C"					
				elif s>=60 and s <=69:
					print "D"					
				elif s <60 and s >=0:
					print "F"					
				else:
					raw_input("invaild score, please input again...") 
		
if __name__ == '__main__':
	score()
'''
#5-4
import os

def runNian():
	while True:
		year = raw_input("Enter a year :")

		if year == 'q':
			quit()
		else:
			try:
				s = int(year)
			except ValueError, e:
				print "Error:",e
				raw_input("please input a year...") 
			else:
				if s>0 :
					if s%4 == 0 and s%100 != 0:
						print "%s 是一个闰年" % s
					elif s%4 == 0 and s%100 == 0:
						print "%s 是一个闰年" % s
					else:
						print "%s 不是闰年" % s
				else:
					raw_input("invaild year, please input again...") 
		
if __name__ == '__main__':
	runNian()