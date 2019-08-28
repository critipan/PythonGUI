# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:10:55 2019
我的第一个窗口
@author: critipan
"""

import tkinter as tk    #导入Tkinter库

window = tk.Tk()#创建窗口对象
window.title('我的第一个窗口')#为窗口设置标题
window.geometry('500x300')#设置窗口大小

#实例化Label对象;bg:背景颜色/font:字体/width：宽度(多少个字符)/height：高度(同上)
label = tk.Label(window, text = '你好，这是一个Label', bg = 'blue', font = ('楷体', 12), width = 30, height = 2)
label.pack()#将Label添加至上层容器 label.pack() label.place()

window.mainloop()#进入消息主循环,当窗口有变化时自动刷新