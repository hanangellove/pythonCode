#/usr/bin/env python
#encoding:utf-8
from Tkinter import * 

top = Tk()
def resize(ev=None):
	label.config(font='Helvetica -%d bold' % scale.get())

def new_file():
	print 'creat a new file'
def open_file():
	print 'open a  file'

mBar = Frame(top,relief=RAISED,borderwidth=2)#先开辟一片区域用于菜单栏的位置
mBar.pack(fill=X)

def makeFileMenu():	
	file_button = Menubutton(mBar,text='File',underline=0)#创建file button
	file_button.pack(side=LEFT,padx='1m')
	file_button.menu = Menu(file_button)#表示file_button有一个下拉菜单

	file_button.menu.add_command(label='New',underline=0,command=new_file)
	file_button.menu.add_command(label='Open',underline=0,command=open_file)
	file_button['menu'] = file_button.menu# set up a pointer from the file menubutton back to the file menu

	return file_button

def makeEditMenu():	
	edit_button = Menubutton(mBar,text='Edit',underline=0)#创建file button
	edit_button.pack(side=LEFT,padx='1m')
	edit_button.menu = Menu(edit_button)#表示file_button有一个下拉菜单

	edit_button.menu.add_command(label='copy',underline=0,)
	edit_button.menu.add_command(label='paste',underline=0,)
	edit_button['menu'] = edit_button.menu# set up a pointer from the file menubutton back to the file menu

	return edit_button

file_button = makeFileMenu()
edit_button = makeEditMenu()
mBar.tk_menuBar(file_button)


label = Label(top,text='Hello World!',bg='black',fg='red',font='Helvetica -12 bold')
entry = Entry()

scale = Scale(top,from_=10, to=40,orient=HORIZONTAL,command=resize)
scale.set(18)#设置进度条的起始默认值

quit = Button(top,text='Quit',command=top.quit)


label.pack(fill=X,expand=1)
entry.pack()
scale.pack(fill=X,expand=1)
quit.pack(expand=1)


mainloop()