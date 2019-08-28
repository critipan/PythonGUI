# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:24:04 2019
练习使用Button
@author: G
"""

#导入库
import tkinter as tk
import time,threading

#实例化窗口
window = tk.Tk()
#为窗口命名
window.title('练习使用Button')
#设置窗口大小
window.geometry('500x300')
#在窗口上添加标签
var = tk.StringVar()#将Label标签的内容设置为字符类型，用Var来接受hit_me传出的内容用以显示在标签上
l = tk.Label(window, textvariable = var, bg = 'green', fg = 'white', font = ('楷体', 12), width = 30, height = 2)
l.pack()

#创建一个新线程，设置var为当前时间
#自定义线程类
class myThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def print_time(threadName = 'print_time'):
        print('线程启动：%s'%(threadName))
        while True:
            s = time.ctime(time.time())
            var.set(s)
            print('%s\t%s'%(threadName,s))
            time.sleep(0.2)

    def run(self):
        print('开始线程:%s'%(self.name))
        print_time(self.name)
        print('结束线程:%s'%(self.name))

#创建并开始线程
thread = myThread(threadID = 1,name = 'Label更新线程')
thread.start()
#定义一个Button的事件方法

def hit_me():
    var.set('you hit me')

        
#实例化Button并将其放入窗口
b = tk.Button(window, text = 'hit me', font = ('Arial', 12 ), width = 10, height = 1, command = hit_me)
b.pack()

#进入主循环
window.mainloop()

