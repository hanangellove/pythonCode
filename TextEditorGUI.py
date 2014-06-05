#!/usr/bin/env python
#encoding:utf-8
__metaclass__ = type
#"文本编辑器，读取，修改，保存文件"

import os
import wx

class TextEditorClass(object):
    #"文本编辑器的类，包含读取文本，修改文本，保存文本的方法"
    def __init__(self):
        #"类的初始化函数，初始基本的数据"
        pass
    def readText(self, event):
        #"读取文本"
        #filename为输入文件编辑框
        #contents为文本编辑框
        with open(self.filename.GetValue()) as fobj:
            self.contents.SetValue(fobj.read())
    def writeText(self, event):
        #"修改文本"
        with open(self.filename.GetValue(), "w") as fobj:
            fobj.write(self.contents.GetValue())
    def guiText(self):
        #"图形界面：文件名输入框，编辑框，读取按钮，写入按钮"
        app = wx.App()
        win = wx.Frame(None, title = "simple editor", size = (410,335))
        win.Show()

        self.filename = wx.TextCtrl(win, pos = (5,5), size = (210, 25))
        self.contents = wx.TextCtrl(win, pos = (5, 35), size = (390, 260),
                               style = wx.TE_MULTILINE | wx.HSCROLL)

        #读取按钮，并且关联读取文件函数
        readButton = wx.Button(win, label = "read", pos = (225,5), size = (80, 25))
        readButton.Bind(wx.EVT_BUTTON, self.readText)
        #写入按钮，并且关联写入文件函数  
        writeButton = wx.Button(win, label = "write", pos = (315, 5), size = (80, 25))
        writeButton.Bind(wx.EVT_BUTTON, self.writeText)
        
        app.MainLoop()

if __name__ == "__main__":
    edit1 = TextEditorClass()
    edit1.guiText()
        
