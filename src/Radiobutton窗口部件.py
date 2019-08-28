# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:35:35 2019

@author: G
"""

#导入库
import tkinter as tk

#实例化窗口
window = tk.Tk()
window.title('Radiobutton窗口部件')
window.geometry('500x300')

#在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()
l = tk.Label(window, bg = 'yellow', width = 20, text ='empty')
l.pack()

#定义选项触发函数
def print_selection():
    l.config(text = 'you have selected '+var.get())
    
#创建三个radiobutton选项，其中variable = var，value='A'意思就是当我们选中了其中一个选项，把value的值放入var，然后赋值给variable
r1 = tk.Radiobutton(window, text = 'Option A', variable = var, value = 'A', command = print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text = 'Option B', variable = var, value = 'B', command = print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text = 'Option C', variable = var, value = 'C', command = print_selection)
r3.pack()

#进入主循环
window.mainloop()