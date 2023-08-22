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

    def clickEncoding(self) :
        for fullname in self.curPaths:
            print(fullname)
            ext = os.path.splitext(fullname)

            options = " -c:v libx264"
            
            if self.Radiobutton_ResolutionVar.get() == 1:
                options = options + " -vf scale=3840:2160"
            elif self.Radiobutton_ResolutionVar.get() == 2:
                options = options + " -vf scale=2560:1440"
            elif self.Radiobutton_ResolutionVar.get() == 3:
                options = options + " -vf scale=1920:1080"

            if self.Radiobutton_CrfVar.get() == 1:
                options = options + " -crf 17"
            elif self.Radiobutton_CrfVar.get() == 2:
                options = options + " -crf 20"
            elif self.Radiobutton_CrfVar.get() == 3:
                options = options + " -crf 23"

            if self.Checkbutton_SlowVar.get() == 1:
                options = options + " -preset veryslow"
            
            cmd = "ffmpeg -i {}{} {}.mp4".format(fullname, options, ext[0])
            # print(cmd)
            os.system(cmd)

    def openFiles(self) :
        self.curPaths = filedialog.askopenfilenames(filetypes=[("webm", ".webm")])
        self.Entry_OpenPath.delete(0, tk.END)
        self.Entry_OpenPath.insert(0, self.curPaths)

    def selectCover(self) :
        print("selectCover ", self.Checkbutton_CoverVar.get())

    def selectSlow(self) :
        print("selectSlow ", self.Checkbutton_SlowVar.get())

    def selectResolution(self) :
        print("selectResolution ", self.Radiobutton_ResolutionVar.get())

    def selectCrf(self) :
        print("selectCrf ", self.Radiobutton_CrfVar.get())

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
        self.Radiobutton_Resolution1 = tk.Radiobutton(self.FM1, text = "4K(3840x2160)", variable = self.Radiobutton_ResolutionVar, value = 1, command = self.selectResolution)
        self.Radiobutton_Resolution1.grid(row = currow, column = 0, sticky = 'nw')
        self.Radiobutton_Resolution2 = tk.Radiobutton(self.FM1, text = "2K(2560x1440)", variable = self.Radiobutton_ResolutionVar, value = 2, command = self.selectResolution)
        self.Radiobutton_Resolution2.grid(row = currow, column = 1, sticky = 'nw')
        self.Radiobutton_Resolution3 = tk.Radiobutton(self.FM1, text = "1080P(1920x1080)", variable = self.Radiobutton_ResolutionVar, value = 3, command = self.selectResolution)
        self.Radiobutton_Resolution3.grid(row = currow, column = 2, sticky = 'nw')

        currow = currow + 1

        self.Radiobutton_CrfVar = tk.IntVar()
        self.Radiobutton_Crf1 = tk.Radiobutton(self.FM1, text = "CRF 17", variable = self.Radiobutton_CrfVar, value = 1, command = self.selectCrf)
        self.Radiobutton_Crf1.grid(row = currow, column = 0, sticky = 'nw')
        self.Radiobutton_Crf2 = tk.Radiobutton(self.FM1, text = "CRF 20", variable = self.Radiobutton_CrfVar, value = 2, command = self.selectCrf)
        self.Radiobutton_Crf2.grid(row = currow, column = 1, sticky = 'nw')
        self.Radiobutton_Crf3 = tk.Radiobutton(self.FM1, text = "CRF 23", variable = self.Radiobutton_CrfVar, value = 3, command = self.selectCrf)
        self.Radiobutton_Crf3.grid(row = currow, column = 2, sticky = 'nw')

        currow = currow + 1

        self.Checkbutton_CoverVar = tk.IntVar()
        self.Checkbutton_Cover = tk.Checkbutton(self.FM1, text = "保留原mp4文件", variable = self.Checkbutton_CoverVar, command = self.selectCover)
        self.Checkbutton_Cover.grid(row = currow, column = 0, sticky = 'nw')

        self.Checkbutton_SlowVar = tk.IntVar()
        self.Checkbutton_Slow = tk.Checkbutton(self.FM1, text = "慢编码（高质量）", variable = self.Checkbutton_SlowVar, command = self.selectSlow)
        self.Checkbutton_Slow.grid(row = currow, column = 1, sticky = 'nw')

        currow = currow + 1
        
        self.Button_Encoding = tk.Button(self.FM1, text = "开始转码", command = self.clickEncoding)
        self.Button_Encoding.grid(row = currow, column = 0, sticky = 'nw')
        

init_window = tk.Tk()
ui = SearchUI(init_window)
ui.initWindow()
init_window.mainloop()
