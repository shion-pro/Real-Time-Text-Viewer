import pathlib
import sys
import os
try:
    current_dir = pathlib.Path(__file__).resolve().parent
except:
    current_dir = os.path.dirname(os.path.abspath('__file__'))

import tkinter as tk
from tkinter import filedialog
import sys

class SbTextFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        text = tk.Text(self,wrap='none',undo=True) #wrapとundo
        text.configure(font=("Courier", 14, "italic")) #font
        #text.configure(state='disabled')
        x_sb = tk.Scrollbar(self,orient='horizontal') #scroll x
        y_sb = tk.Scrollbar(self,orient='vertical') #scroll y
        x_sb.config(command=text.xview)
        y_sb.config(command=text.yview)
        text.config(xscrollcommand=x_sb.set,yscrollcommand=y_sb.set)
        text.grid(column=0,row=0,sticky='nsew')
        x_sb.grid(column=0,row=1,sticky='ew')
        y_sb.grid(column=1,row=0,sticky='ns')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.text = text
        self.x_sb = x_sb
        self.y_sb = y_sb


def fileopen():
    global fname,textframe,root
    fname = filedialog.askopenfilename()
    if fname == "":
        pass
    else:
        f = open(fname,'r')
        lines = f.readlines()
        f.close()
        textframe.text.delete('1.0','end')
        for line in lines:
            textframe.text.insert('end',line)
        root.title('Real Time Text Viewer - '+fname)
        root.after(1000, draw)

def filesave():
    global fname,textframe
    if fname == '':
        return
    f = open(fname,'w')
    lines = textframe.text.get('1.0','end-1c')
    f.writelines(lines)
    f.close()

def exit():
    root.destroy()
    sys.exit()


def draw():
    f = open(fname,'r')
    lines = f.readlines()
    f.close()
    textframe.text.delete('1.0','end')
    for line in lines:
        textframe.text.insert('end',line)
    textframe.text.see("{}.0".format(len(lines)-1))
    root.after(100, draw)

def main():
    global fname,textframe,root
    fname = ''
    root = tk.Tk()
    root.title('Real Time Text Viewer')
    root.geometry('1000x500')
    textframe = SbTextFrame(root)
    textframe.pack(side='top',fill='both',expand=True)
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar,tearoff=0)

    filemenu.add_command(label='Open',command=fileopen)
    # filemenu.add_command(label='Save',command=filesave)
    # filemenu.add_command(label='Exit',command=exit)
    menubar.add_cascade(label='File',menu=filemenu)
    root.config(menu=menubar)
    root.mainloop()

main()
