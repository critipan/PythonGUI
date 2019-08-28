# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:46:12 2019

@author: G
"""

#导入库
import tkinter as tk

window = tk.Tk()
window.title('Checkbutton窗口部件')
window.geometry('500x300')

#在图形界面上创建一个标label用以显示并放置
l = tk.Label(window, bg = 'yellow', width = '20', text = 'empty')
l.pack()

#定义触发函数
def print_selection():
    if (var1.get() == 1)&(var2.get() == 0 ):
        l.config(text = 'I love only Python ')
    elif (var1.get() == 0)&(var2.get() == 1):
        l.config(text = 'I love only C++ ')
    else:
        l.config(text = 'I love both ')
        
#定义两个Checkbutton并放置
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text = 'Python', variable = var1, onvalue = 1, offvalue = 0, command = print_selection)
c2 = tk.Checkbutton(window, text = 'C++', variable = var2, onvalue = 1, offvalue = 0, command = print_selection)
c1.pack()
c2.pack()


#进入主循环
window.mainloop()