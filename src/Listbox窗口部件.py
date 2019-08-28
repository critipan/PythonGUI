# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:49:06 2019

@author: G
"""

#导入库
import tkinter as tk

#实例化窗口
window = tk.Tk()
#为窗口命名
window.title('Listbox窗口部件')
#设置大小
window.geometry('500x300')
#在图形界面上创建一个标签label用以显示并放置
var1 = tk.StringVar()
l = tk.Label(window, bg = 'green', fg = 'yellow', font = ('Arial', 12), width = 10, textvariable =var1)
l.pack()
#创建一个方法用于按钮的点击事件
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)#为Label设置值
    
#创建一个按钮并防止，点击按钮调用print_selection函数
b1 = tk.Button(window,text= 'print selection', width = 15, height = 2, command = print_selection)
b1.pack()

#创建Listbox并添加内容
var2 = tk.StringVar()
var2.set((1,2,3,4))#为变量var2设置值
lb = tk.Listbox(window, listvariable = var2)#将var2的值赋给Listbox
#创建一个List并将值循环添加至Listbox中
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end',item)
    
lb.pack()

#进入主循环
window.mainloop()