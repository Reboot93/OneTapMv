import os
import shutil
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('手机图片一键移动到电脑_V0.1')
root.geometry('1100x800')
bt1_jpg = tk.PhotoImage(file='bt1.png')
bt2_jpg = tk.PhotoImage(file='bt2.png')
DCIM_Dir = ''
WeiXin_Dir = ''
PC_DCIM_Dir = ''
PC_WeiXin_Dir = ''


def HowToMv(msg):
    global DCIM_Dir, mv_dir
    global DCIM_list
    global PC_DCIM_Dir
    global PC_DCIM_Dir_list
    global WeiXin_Dir
    global WeiXin_list
    global PC_WeiXin_Dir
    global PC_WeiXin_Dir_list

    if msg == 1:
        mv_dir = str(DCIM_Dir)
    if msg == 2:
        mv_dir = str(WeiXin_Dir)
    file_name = os.listdir(mv_dir)
    for filename in file_name:
        old_name = os.path.join(mv_dir, filename)
        if os.path.isfile(old_name):
            if msg == 1:
                shutil.move(old_name, os.path.join(PC_DCIM_Dir, filename))
            if msg == 2:
                shutil.move(old_name, os.path.join(PC_WeiXin_Dir, filename))
        else:
            pass


def get_file_dir(msg):  # 目录设置函数
    global SecScreen
    global DCIM_Dir
    global DCIM_list
    global PC_DCIM_Dir
    global PC_DCIM_Dir_list
    global WeiXin_Dir
    global WeiXin_list
    global PC_WeiXin_Dir
    global PC_WeiXin_Dir_list
    global file_dir
    SecScreen.wm_attributes('-topmost', 0)
    file_dir = filedialog.askdirectory()
    if msg == 1:
        DCIM_list.insert(0, file_dir)  # 将文件夹位置嵌入列表中以进行显示（下同上）
        DCIM_Dir = file_dir
    if msg == 2:
        WeiXin_list.insert(0, file_dir)
        WeiXin_Dir = file_dir
    if msg == 3:
        PC_DCIM_Dir_list.insert(0, file_dir)
        PC_DCIM_Dir = file_dir
    if msg == 4:
        PC_WeiXin_Dir_list.insert(0, file_dir)
        PC_WeiXin_Dir = file_dir
    else:
        pass
    SecScreen.wm_attributes('-topmost', 1)


def SetDir():  # 目录设置窗口函数
    global SecScreen
    global DCIM_Dir
    global DCIM_list
    global PC_DCIM_Dir
    global PC_DCIM_Dir_list
    global WeiXin_Dir
    global WeiXin_list
    global PC_WeiXin_Dir
    global PC_WeiXin_Dir_list

    SecScreen = tk.Tk()
    SecScreen.wm_attributes('-topmost', 1)  # 将窗口置顶
    SecScreen.title('目录设置')

    DCIM_text = tk.Label(SecScreen, text='手机照片目录')
    WeiXin_text = tk.Label(SecScreen, text='微信照片目录')
    DCIM_list = tk.Listbox(SecScreen, height='1', width='50')
    DCIM_list.insert(0, DCIM_Dir)
    DCIM_ENTER = tk.Button(SecScreen, text='选择目录', command=lambda: get_file_dir(1))
    WeiXin_list = tk.Listbox(SecScreen, height='1', width='50')
    WeiXin_list.insert(0, WeiXin_Dir)
    WeiXin_ENTER = tk.Button(SecScreen, text='选择目录', command=lambda: get_file_dir(2))
    PC_DCIM_Dir_text = tk.Label(SecScreen, text='电脑端手机照片存放目录')
    PC_WeiXin_Dir_text = tk.Label(SecScreen, text='电脑端照片存放目录')
    PC_DCIM_Dir_list = tk.Listbox(SecScreen, height='1', width='50')
    PC_DCIM_Dir_list.insert(0, PC_DCIM_Dir)
    PC_DCIM_Dir_ENTER = tk.Button(SecScreen, text='选择目录', command=lambda: get_file_dir(3))
    PC_WeiXin_Dir_list = tk.Listbox(SecScreen, height='1', width='50')
    PC_WeiXin_Dir_list.insert(0, PC_WeiXin_Dir)
    PC_WeiXin_Dir_ENTER = tk.Button(SecScreen, text='选择目录', command=lambda: get_file_dir(4))

    DCIM_text.grid(row=0, column=0)
    DCIM_ENTER.grid(row=0, column=1)
    DCIM_list.grid(row=0, column=2)
    WeiXin_text.grid(row=1, column=0)
    WeiXin_ENTER.grid(row=1, column=1)
    WeiXin_list.grid(row=1, column=2)
    PC_DCIM_Dir_text.grid(row=2, column=0)
    PC_DCIM_Dir_ENTER.grid(row=2, column=1)
    PC_DCIM_Dir_list.grid(row=2, column=2)
    PC_WeiXin_Dir_text.grid(row=3, column=0)
    PC_WeiXin_Dir_ENTER.grid(row=3, column=1)
    PC_WeiXin_Dir_list.grid(row=3, column=2)

    SecScreen.mainloop()


# ========================================================================================================

DCIM_b = tk.Button(root, image=bt1_jpg, command=lambda: HowToMv(1))
WeiXin_b = tk.Button(root, image=bt2_jpg, command=lambda: HowToMv(2))
Set_b = tk.Button(root, text='目录设置', command=SetDir)

DCIM_b.place(x=50, y=100)
WeiXin_b.place(x=570, y=100)
Set_b.place(x=950, y=40)

root.mainloop()  # 主窗口循环
