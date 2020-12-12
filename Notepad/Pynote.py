"""
Author : Siddharth Sharma
Date : 8/10/2020

import tkinter as Tk
import os
from tkinter import *

from tkinter.messagebox import *

from tkinter.filedialog import *


class Notepad:
    __root = Tk()
    
    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff= 0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    
    # to add scroll bar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None
    
    def __init__(self, **kwargs):
        
        # set icon
        try:
            self.__root.wm_iconbitmap('Notepad.ico')
        except:
            pass
        
        # set window size
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
        
        # set the windows title
        self.__root.title('Untitle - Notepad')
        
        # center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        
        # for left-align
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenWidth / 2) - (self.__thisHeight / 2)
        
        # for top and bottom
        self.__root.geometry("%dx%d+%d+%d"% (self.__thisWidth, self.__thisHeight, left, top))
        
        # to make the text area auto resizeable
        self.__root.grid_rowconfigure(0, weight = 1)
        self.__root.grid_columnconfigure(0, weight = 1)
        
        # add controls widget
        self.__thisTextArea.grid(sticky = N + E + S + W) 
        
        # to open new file
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        
        # to open already existing file
        self.__thisFileMenu.add_command(label='open', command=self.__openFile)
        
        # to save current file
        self.__thisFileMenu.add_command(label='save', command=self.__saveFile)
        
        # to crate a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Quit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)
        
        # to give a feature of cut
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        
        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        
        # to give a feature of paste
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        
        # to give a feature of editing
        self.__thisEditMenu.add_command(label="Edit", command=self.__thisEditMenu)
        
        # to give a feature of description of the notepad
        # self.__thisHelpMenu.add_command(label="About", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", command=self.__showAbout)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        
        # scrollbar willadjust automatically sccording to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        
    def __quitApplication(self):
            self.__root.destroy()
            #exit
    def __showAbout(self):
            showinfo('Notepad','Notepad created by Siddharth Sharma')
            
    def __openFile(self):
        self.__file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*" ), ("Text Documentd", "*..txt")])
            
        if self.__file == "":
            # no file to open
            self.__file = None
            
        else:
            # try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + "- Notepad")
            self.__thisTextArea.delete(1.0, END)
                
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()
                
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)
            
    def __saveFile(self):
        if self.__file == None:
             # save as new file
            self.__file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
                
            if self.__file == "":
                self.__file = None
            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0 , END))
                file.close()
                    
                # change the window title
                self.__root.title(os.path.basename(self.__file) + "- Notepad")
            
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()
        
    def __cut(self):
        self.__thisTextArea.event_generate("<<CUt>>")
            
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
            
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
        
    def run(self):
        # run main application
        self.__root.mainloop()
            
 
                    
notepad = Notepad(width=600, height=400)
notepad.run()        
        
        
