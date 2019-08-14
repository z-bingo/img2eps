import os, sys
from tkinter import Tk, Button, Label, Text
from tkinter.filedialog import *
from PIL import Image

filetype = ('.jpg', '.bmp', '.png')

all_files = []
path = None

def getPath():
    global path
    path = askdirectory()
    entry.delete(0, END)
    entry.insert(0, path)
    files = os.listdir(path)
    for p in files:
        p_split = os.path.splitext(p)
        if p_split[-1].lower() in filetype:
            all_files.append(p)
    label_text.set("All Files:\n" + '\n'.join(all_files))

def startConvert():
    global path
    for f in all_files:
        f_split = os.path.splitext(f)
        label_text.set('Processing {} ...\n'.format(f) + label_text.get())
        img = Image.open(os.path.join(path, f))
        img.save('{}.eps'.format(os.path.join(path, f_split[-2])), 'EPS')
        label_text.set('Processing {} done!\n'.format(f) + label_text.get())
    label_text.set('All images have been converted OK!\n' + label_text.get())

win = Tk()
win.title('img2eps')
win.geometry('450x250')
win.maxsize(width=450, height=250)

Label(win, text='当前路径: ', height=1).place(x=40, y=20, anchor='c')
entry = Entry(win, state='normal', width=30)
entry.place(x=220, y=20, anchor='c', width=300)
button_open = Button(win, text='选择路径', height=1, command=getPath)
button_open.place(x=410, y=20, anchor='c')

button_start = Button(win, text="开始转换", height=2, width=8,  command=startConvert)
button_start.place(x=370, y=80, anchor='c')

label_text = StringVar()
files = Label(win, state='normal', height=11, width=40, textvariable=label_text, justify='left', anchor='nw', bg='lightgray')
files.place(x=10, y=50, anchor='nw')

Label(win, text="-支持jpg, bmp, png三种\n格式的图片;\n\n-使用时，通过[选择路径]\n按钮选中图片所在路径，\n继续点击[开始转换]即可。", width=19, height=7, justify='left', anchor='nw', bg='lightgray').\
    place(x=302, y=118, anchor='nw')


win.mainloop()
