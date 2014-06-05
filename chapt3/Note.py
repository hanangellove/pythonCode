#!/usr/bin/env python
#encoding:utf-8

#TextEditor

import sys,os
import tkFileDialog
from Tkinter import *

class Note():
	"""This is a text Editor"""
	def __init__(self):
		self.tk=Tk()
		self.createUI()
		self.tk.mainloop()

	def createUI(self):
		menubar = Menu(self.tk)
		fmenu = Menu(menubar,tearoff=0)
		menubar.add_cascade(label='File',menu=fmenu)
		#fmenu.add_command(label='New',command=self.new)
		fmenu.add_command(label='Open',command=self.open)
		fmenu.add_command(label='Save',command=self.save)
		fmenu.add_command(label='Exit',command=self.exit)

		self.tk.config(menu=menubar)
		self.text=Text()
		self.text.pack()
	'''
	def new(self):
		self.text=Text()
		self.text.pack()
	'''

	def save(self):
		txtContent = self.text.get(1.0,END)
		self.saveFile(content=txtContent)

	def open(self):
		self.filename = tkFileDialog.askopenfilename(initialdir=os.getcwd())
		filecontent = self.openFile(fname = self.filename)
		if filecontent is not -1:
			self.text.delete(1.0,END)
			self.text.insert(1.0,filecontent)


	def openFile(self,fname=None):
		if fname is None:
			return -1

		self.fname = fname
		file = open(fname,"r+")
		content = file.read()
		file.close()
		return content

	def saveFile(self,content=None):
		if content is None:
			return -1

		file = open(fname,'w')
		file.write(content)
		file.flush()
		file.close()
		return 0

	def exit(self):
		sys.exit(0)
if __name__ == '__main__':
		Note()	

