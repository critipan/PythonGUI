# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:27:26 2019

@author: G
"""

#导入库
import tkinter as tk

#实例化窗口
window = tk.Tk()
#命名
window.title('Text窗口部件')
#设置大小
window.geometry('500x300')
#添加Entry
e = tk.Entry(window, show = None)
e.pack()

#定义两个事件触发函数
def insert_point():
    '在鼠标焦点处插入内容'
    var = e.get()
    t.insert('insert',var)
def insert_end():
    '在文本框最后添加内容'
    var = e.get()
    t.insert('end',var)

#创建两个按钮
b1 = tk.Button(window, text = '在光标处插入', width = 10, height = 2, command = insert_point)
b2 = tk.Button(window, text = '在结尾处插入', width = 10, height = 2, command = insert_end)
b1.pack()
b2.pack()
N
#创建Text
t = tk.Text(window)
t.pack()

#进入主循环
window.mainloop()