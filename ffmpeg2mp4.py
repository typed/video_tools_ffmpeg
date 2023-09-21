#!/usr/bin/python
#encoding: utf-8

import os
import sys
import time
import tkinter as tk
from tkinter import filedialog

search_root = '../'

class VideoUI() :
    def __init__(self, init_window) :
        self.init_window = init_window
        self.optionCodec = (("h264", "-c:v libx264"), ("h265", "-c:v libx265"))
        self.optionExt = (("mp4", "mp4"), ("mov", "mov"))
        self.optionCrf = (("CRF23", "-crf 23"), ("CRF20", "-crf 20"), ("CRF17", "-crf 17"))
        self.optionResolution = (("4K(3840x2160)", "-vf scale=3840:2160"), ("2K(2560x1440)", "-vf scale=2560:1440"), ("1080P(1920x1080)", "-vf scale=1920:1080"), ("720P(1280x720)", "-vf scale=1280:720"))

    def clickEncoding(self) :
        for fullname in self.curPaths:
            print(fullname)
            ext = os.path.splitext(fullname)
            suffix = ""
            if self.Checkbutton_SuffixVar.get() == 1:
                suffixVar = self.Entry_SuffixVar.get()
                if len(suffixVar) > 0:
                    suffix = "_{}".format(suffixVar)
            options = ""
            options = options + " " + self.optionCodec[self.Radiobutton_CodecVar.get()][1]
            # Video Filters
            options = options + " " + self.optionResolution[self.Radiobutton_ResolutionVar.get()][1]
            if self.Checkbutton_HdrToSdrVar.get() == 1:
                options = options + ",zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"

            options = options + " " + self.optionCrf[self.Radiobutton_CrfVar.get()][1]
            if self.Checkbutton_SlowVar.get() == 1:
                options = options + " -preset veryslow"
            extname = self.optionExt[self.Radiobutton_ExtVar.get()][1]
            cmd = "ffmpeg -i \"{}\"{} \"{}{}.{}\"".format(fullname, options, ext[0], suffix, extname)
            print(cmd)
            os.system(cmd)

    def openFiles(self) :
        self.curPaths = filedialog.askopenfilenames()
        self.Entry_OpenPath.delete(0, tk.END)
        self.Entry_OpenPath.insert(0, self.curPaths)

    def selectCodec(self) :
        print("selectCodec ", self.optionCodec[self.Radiobutton_CodecVar.get()])
    
    def selectExt(self) :
        print("selectExt ", self.optionExt[self.Radiobutton_ExtVar.get()])

    def selectSuffix(self) :
        print("selectSuffix ", self.Checkbutton_SuffixVar.get())

    def selectSlow(self) :
        print("selectSlow ", self.Checkbutton_SlowVar.get())

    def selectHdrToSdr(self) :
        print("selectHdrToSdr ", self.Checkbutton_HdrToSdrVar.get())

    def selectResolution(self) :
        print("selectResolution ", self.optionResolution[self.Radiobutton_ResolutionVar.get()])

    def selectCrf(self) :
        print("selectCrf ", self.optionCrf[self.Radiobutton_CrfVar.get()])

    def initWindow(self) :

        self.init_window.title("ffmpeg转mp4")
        window_width = 600
        window_height = 500
        screenwidth = self.init_window.winfo_screenwidth()
        screenheight = self.init_window.winfo_screenheight()
        size = "%dx%d+%d+%d" % (window_width, window_height, (screenwidth - window_width)/2, (screenheight - window_height)/2)
        self.init_window.geometry(size)

        currow = 0
        
        self.FM1 = tk.Frame(self.init_window, borderwidth = 10)
        self.FM1.grid(row = currow, column = 0, sticky = 'nw')

        self.Button_OpenFile = tk.Button(self.FM1, text = "打开多个文件", command = self.openFiles)
        self.Button_OpenFile.grid(row = currow, column = 0, sticky = 'nw')
        
        self.Entry_OpenPath = tk.Entry(self.FM1)
        self.Entry_OpenPath.grid(row = currow, column = 1, columnspan = 4, sticky = 'nesw')

        currow = currow + 1

        self.Radiobutton_CodecVar = tk.IntVar()
        for idx in range(len(self.optionCodec)):
            itm = self.optionCodec[idx]
            radio = tk.Radiobutton(self.FM1, text = itm[0], variable = self.Radiobutton_CodecVar, value = idx, command = self.selectCodec)
            radio.grid(row = currow, column = idx, sticky = 'nw')

        currow = currow + 1

        self.Radiobutton_ExtVar = tk.IntVar()
        for idx in range(len(self.optionExt)):
            itm = self.optionExt[idx]
            radio = tk.Radiobutton(self.FM1, text = itm[0], variable = self.Radiobutton_ExtVar, value = idx, command = self.selectExt)
            radio.grid(row = currow, column = idx, sticky = 'nw')

        currow = currow + 1

        self.Radiobutton_ResolutionVar = tk.IntVar()
        self.Radiobutton_ResolutionVar.set(2)
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

        self.Checkbutton_SlowVar = tk.IntVar()
        self.Checkbutton_SlowVar.set(1)
        checkBtn = tk.Checkbutton(self.FM1, text = "慢编码（高质量）", variable = self.Checkbutton_SlowVar, command = self.selectSlow)
        checkBtn.grid(row = currow, column = 0, sticky = 'nw')

        self.Checkbutton_HdrToSdrVar = tk.IntVar()
        self.Checkbutton_HdrToSdrVar.set(1)
        checkBtn = tk.Checkbutton(self.FM1, text = "HDR转SDR", variable = self.Checkbutton_HdrToSdrVar, command = self.selectHdrToSdr)
        checkBtn.grid(row = currow, column = 1, sticky = 'nw')

        currow = currow + 1

        self.Checkbutton_SuffixVar = tk.IntVar()
        checkBtn = tk.Checkbutton(self.FM1, text = "加后缀", variable = self.Checkbutton_SuffixVar, command = self.selectSuffix)
        checkBtn.grid(row = currow, column = 0, sticky = 'nw')
        self.Entry_SuffixVar = tk.StringVar()
        entrySuffix = tk.Entry(self.FM1, textvariable = self.Entry_SuffixVar)
        entrySuffix.grid(row = currow, column = 1, columnspan = 1, sticky = 'nesw')

        currow = currow + 1
        
        self.Button_Encoding = tk.Button(self.FM1, text = "开始转码", command = self.clickEncoding)
        self.Button_Encoding.grid(row = currow, column = 0, sticky = 'nw')
        

init_window = tk.Tk()
ui = VideoUI(init_window)
ui.initWindow()
init_window.mainloop()
