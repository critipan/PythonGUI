# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:19:06 2019

@author: G
"""
#导入库
import tkinter as tk

#实例化窗口
window = tk.Tk()
#为窗口命名
window.title('Entry窗口部件')
#设置窗口大小
window.geometry('500x300')
#实例化Entry并放入上层容器
e1 = tk.Entry(window, show = '*', font = ('Arial',14))
e2 = tk.Entry(window, show = None, font = ('Arial',14))
e1.pack()
e2.pack()

#进入主循环
window.mainloop()