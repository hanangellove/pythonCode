#!/usr/bin/ python
# encoding:utf-8
'''
#2-4
a = raw_input("Enter something:")
b = int(a)
print b

#2-5

i = 0
while(i<11):
    print i,
    i+=1
print "\n"
for i in range(11):
    print i,
print '\n'
    
#2-6
a = int(raw_input("Enter your number:\n"))
if a>0:
	print "这是一个正数"
else:
	print "这是一个负数"


#2-7
str = str(raw_input('Enter your string:'))
i = 0
while i<len(str):
    print str[i],
    i += 1
print '\n'
for item in str:
    print item,
print "\n"
for k in enumerate(str):
    print k,
'''
'''
#2-8
i = 0
k = 0
#alist1 = [3,-1,23,5,9]
alist1 = []
for i in range(5):
    x = int(raw_input('Enter a number:'))
    alist1.append(x)
print 'the alist is:'alist1
print "the length of alist1 is :",len(alist1)

sum = 0
while k<len(alist1):
    sum = sum + alist1[k]
   # print sum
    k+=1
print sum
print "\n"

sum = 0
for item in alist1:
    sum = sum + item
print sum
print "\n"

#2-9
i = 0
k = 0
alist1 = [3,-1,23,5,9]
sum = 0
while k<len(alist1):
    sum = sum + alist1[k]
   # print sum
    k+=1
ave = float(sum)/float(len(alist1))
print 'sum is %d, average is :%f' % (sum, ave)
print "\n"

#2-10
bl = True

while bl:
    a = int(raw_input("Enter a number:"))
    if a>1&a<100:
        print "恭喜，输入正确！"
        break
    else:
        print"输入错误，请重新输入！"

#2-11
def inputNum():
    alist = []
    for i in range(5):
        x = int(raw_input('Enter a number:'))
        alist.append(x)
    print 'the alist is:',alist
    print "the length of alist1 is :",len(alist)
    return alist

def sumNum(alist):
    sum = 0
    for item in alist:
        sum = sum + item
    print sum
    return sum
    print "\n"
    
def aveNum(alist):
    k = 0
    sum = 0
    while k<len(alist):
        sum = sum + alist[k]
       # print sum
        k+=1
    ave = float(sum)/float(len(alist))
    print 'sum is %d, average is :%f' % (sum, ave)
    print "\n"
    
def main():
   myalist = inputNum()
   while True:
        print '-------WOW--------'
        print '1：求五个数的和'
        print '2：求五个数的平均数'
        print 'X：退出'
        choose = raw_input( '您想要做什么呢:')
        if choose == '1':
            sumNum(myalist)
        elif choose == '2':
            aveNum(myalist)
        elif choose == 'X' or choose == 'x':
            quit()
        else :
            print('输入错误，请重新选择！')
        print "\n"
if __name__ == '__main__':
    main()

#2-15
while True:
    x = raw_input('Enter a number:')
    y = raw_input('Enter a number:')
    z = raw_input('Enter a number:')

    max = 0
    if x > y > z :
        print x,y,z,
    elif x > z > y:
        print x,z,y,
    elif y > x > z :
        print y,x,z,
    elif y > z > x :
        print y,z,x,
    elif z > x > y :
        print z,x,y,
    elif z > y > x :
        print z,y,x,
    else :
        print 'they are same~!' ,(x,y,z)
        quit()
    print'\n'
'''
#2-16
filename = raw_input('Enter file name:')
fobj = open(filename,'r')
for eachline in fobj:
    print eachline
fobj.close()




