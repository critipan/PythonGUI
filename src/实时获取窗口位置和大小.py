# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:25:39 2019

@author: G
"""

#导入库
import tkinter as tk

def update_window_configure(event):
    x,y = event.x,event.y
    width,height = event.width, event.height
    print('\b'*80, end = '', flush = True)#清空当前行
    print('position : (%d,%d)\tsize :(%d,%d)'%(x,y,width,height))
    
window = tk.Tk()
window.title('实时获取窗口大小和位置')
window.geometry('500x300')
window.bind('<Configure>', update_window_configure)#将窗口绑定配置事件(Configure),每次触发Configure事件都会调用update_wiondow_configure函数
window.mainloop()