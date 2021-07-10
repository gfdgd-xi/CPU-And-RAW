#!/usr/bin/env python3

import os
import sys
import time
import random
import psutil
import ttkthemes
import traceback
import threading
import webbrowser
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

def Run():
    global close
    global progressbar1
    while not close:
        try:
            CPU = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            labelText1.set("CPU 使用率：{}%".format(str(CPU)))
            labelText2.set("内存使用率：{}%".format(str(memory)))
            progressbar1['value'] = CPU
            progressbar2['value'] = memory
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=traceback.format_exc)
        time.sleep(1)

def CloseWindow():
    global close
    ans = messagebox.askokcancel(title="提示", message="确定要退出吗？")
    if ans:
        close = True
        window.destroy()
    else:
        return

def xShowMenu(event):
    menu.post(event.x_root, event.y_root)   # #将菜单条绑定上事件，坐标为x和y的root位置

# 显示“关于这个程序”窗口
def about_this_program():
    global about
    global title
    global iconPath
    mess = tk.Toplevel()
    message = ttk.Frame(mess)
    mess.resizable(0, 0)
    mess.title("关于 {}".format(title))
    #mess.iconphoto(False, tk.PhotoImage(file=iconPath))
    #img = ImageTk.PhotoImage(Image.open(iconPath))
    #label1 = ttk.Label(message, image=img)
    label2 = ttk.Label(message, text=about)
    button1 = ttk.Button(message, text="确定", command=mess.withdraw)
    #label1.pack()
    label2.pack()
    button1.pack(side="bottom")
    message.pack()
    mess.mainloop()

# 重启本应用程序
def ReStartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# 显示“提示”窗口
def helps():
    global tips
    messagebox.showinfo(title="提示", message=tips)

# 显示更新内容窗口
def UpdateThings():
    messagebox.showinfo(title="更新内容", message=updateThings)

# 打开程序官网
def OpenProgramURL():
    webbrowser.open_new_tab(programUrl)

###########################
# 程序信息
###########################
programUrl = "https://gitee.com/gfdgd-xi/CPU-And-RAW"
version = "1.0.0"
goodRunSystem = "Windows、Linux"
about = '''一个基于 Python3 的 tkinter 制作的系统资源查看小工具
版本：{}
适用平台：{}
tkinter 版本：{}
程序官网：{}
©2021-{} gfdgd xi'''.format(version, goodRunSystem, tk.TkVersion, programUrl, time.strftime("%Y"))
tips = '''提示：无'''
updateThingsString = '''更新内容：无'''
title = "系统资源查看小工具 {}".format(version)
updateTime = "2021年7月10日"
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
iconPath = "{}/icon.png".format(os.path.split(os.path.realpath(__file__))[0])

###########################
# 设置变量
###########################
close = False
themes = ttkthemes.THEMES
themesName = themes[random.randint(0, len(themes) - 1)]

###########################
# 窗口创建
###########################
window = tk.Tk()
win = ttk.Frame(window)
labelText1 = tk.StringVar()
labelText2 = tk.StringVar()
labelText1.set("CPU 使用率：0%")
labelText2.set("内存使用率：0%")
label1 = ttk.Label(win, textvariable=labelText1)
label2 = ttk.Label(win, textvariable=labelText2)
progressbar1 = ttk.Progressbar(win)
progressbar2 = ttk.Progressbar(win)
button1 = ttk.Button(win, text="退出", command=CloseWindow)
menu = tk.Menu(win)
menu.add_command(label="打开官网", command=OpenProgramURL)
menu.add_command(label="更新内容", command=UpdateThings)
menu.add_command(label="提示", command=helps)
menu.add_command(label="关于", command=about_this_program)
menu.add_separator()
menu.add_command(label="重启程序", command=ReStartProgram)
menu.add_separator()
menu.add_command(label="退出", command=CloseWindow)
window.bind("<Button-3>", xShowMenu)     # #设定鼠标右键触发事件，调用xShowMenu方法
window.protocol('WM_DELETE_WINDOW', CloseWindow)
progressbar1['maximum'] = 100
progressbar2['maximum'] = 100
#win.iconphoto(False, tk.PhotoImage(file=iconPath))
window.wm_attributes('-topmost', 1)
window.title(title)
window.attributes('-alpha', 0.5)
window.resizable(0, 0)
style = ttkthemes.ThemedStyle(window)
style.set_theme(themesName)
threading.Thread(target=Run).start()
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
progressbar1.grid(row=0, column=1)
progressbar2.grid(row=1, column=1)
button1.grid(row=2, column=0, columnspan=2)
win.pack()
window.mainloop()
