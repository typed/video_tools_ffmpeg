#!/usr/bin/python
#encoding: utf-8

import os
import sys
import time
import tkinter as tk
from tkinter import filedialog

search_root = '../'

class SearchUI() :
    def __init__(self, init_window) :
        self.init_window = init_window
        self.search_content = tk.StringVar(self.init_window, "")
        self.optionCrf = (("CRF23", " -crf 23"), ("CRF20", " -crf 20"), ("CRF17", " -crf 17"))
        self.optionResolution = (("4K(3840x2160)", " -vf scale=3840:2160"), ("2K(2560x1440)", " -vf scale=2560:1440"), ("1080P(1920x1080)", " -vf scale=1920:1080"))

    def clickEncoding(self) :
        for fullname in self.curPaths:
            print(fullname)
            ext = os.path.splitext(fullname)
            suffix = ""
            if self.Checkbutton_SuffixVar.get() == 1:
                suffix = "_{}_{}".format(self.optionResolution[self.Radiobutton_ResolutionVar.get()][0], self.optionCrf[self.Radiobutton_CrfVar.get()][0])
            options = " -c:v libx264"
            options = options + self.optionResolution[self.Radiobutton_ResolutionVar.get()][1]
            options = options + self.optionCrf[self.Radiobutton_CrfVar.get()][1]
            if self.Checkbutton_SlowVar.get() == 1:
                options = options + " -preset veryslow"
            cmd = "ffmpeg -i {}{} {}{}.mp4".format(fullname, options, ext[0], suffix)
            print(cmd)
            # os.system(cmd)

    def openFiles(self) :
        self.curPaths = filedialog.askopenfilenames()
        self.Entry_OpenPath.delete(0, tk.END)
        self.Entry_OpenPath.insert(0, self.curPaths)

    def selectSuffix(self) :
        print("selectSuffix ", self.Checkbutton_SuffixVar.get())

    def selectSlow(self) :
        print("selectSlow ", self.Checkbutton_SlowVar.get())

    def selectResolution(self) :
        print("selectResolution ", self.optionResolution[self.Radiobutton_ResolutionVar.get()])

    def selectCrf(self) :
        print("selectCrf ", self.optionCrf[self.Radiobutton_CrfVar.get()])

    def initWindow(self) :

        currow = 0
        self.init_window.title("ffmpeg转mp4")
        self.init_window.geometry('600x500+10+10')
        
        self.FM1 = tk.Frame(self.init_window, borderwidth = 10)
        self.FM1.grid(row = currow, column = 0, sticky = 'nw')

        self.Button_OpenFile = tk.Button(self.FM1, text = "打开多个文件", command = self.openFiles)
        self.Button_OpenFile.grid(row = currow, column = 0, sticky = 'nw')
        
        self.Entry_OpenPath = tk.Entry(self.FM1)
        self.Entry_OpenPath.grid(row = currow, column = 1, columnspan = 4, sticky = 'nesw')

        currow = currow + 1

        self.Radiobutton_ResolutionVar = tk.IntVar()
        for idx in range(len(self.optionResolution)):
            itm = self.optionResolution[idx]
            radio = tk.Radiobutton(self.FM1, text = itm[0], variable = self.Radiobutton_ResolutionVar, value = idx, command = self.selectResolution)
            radio.grid(row = currow, column = idx, sticky = 'nw')

        currow = currow + 1

        self.Radiobutton_CrfVar = tk.IntVar()
        for idx in range(len(self.optionCrf)):
            itm = self.optionCrf[idx]
            radio = tk.Radiobutton(self.FM1, text = itm[0], variable = self.Radiobutton_CrfVar, value = idx, command = self.selectCrf)
            radio.grid(row = currow, column = idx, sticky = 'nw')

        currow = currow + 1

        self.Checkbutton_SuffixVar = tk.IntVar()
        checkBtn = tk.Checkbutton(self.FM1, text = "加后缀", variable = self.Checkbutton_SuffixVar, command = self.selectSuffix)
        checkBtn.grid(row = currow, column = 0, sticky = 'nw')

        self.Checkbutton_SlowVar = tk.IntVar()
        checkBtn = tk.Checkbutton(self.FM1, text = "慢编码（高质量）", variable = self.Checkbutton_SlowVar, command = self.selectSlow)
        checkBtn.grid(row = currow, column = 1, sticky = 'nw')

        currow = currow + 1
        
        self.Button_Encoding = tk.Button(self.FM1, text = "开始转码", command = self.clickEncoding)
        self.Button_Encoding.grid(row = currow, column = 0, sticky = 'nw')
        

init_window = tk.Tk()
ui = SearchUI(init_window)
ui.initWindow()
init_window.mainloop()
