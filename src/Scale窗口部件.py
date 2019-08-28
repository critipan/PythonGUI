# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:34:22 2019

@author: G
"""

import tkinter as tk

window = tk.Tk()
window.title('Scale窗口部件')
window.geometry('500x300')

#在界面上创建一个Label用以显示并放置
l = tk.Label(window, bg = 'green', fg = 'white', width = 20, text = 'empty')
l.pack()

#定义一个触发函数
def print_selection(v):
    l.config(text = 'you have selected '+ v)
    
#创建一个滑块
s = tk.Scale(window, label = 'try me', from_=0,to=10,orient=tk.HORIZONTAL,length=200,showvalue=0,tickinterval = 2,resolution = 0.01,command = print_selection)
s.pack()

#进入主循环
window.mainloop()