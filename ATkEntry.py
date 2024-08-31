#!/usr/bin/python3
import tkinter
import customtkinter
from awesometkinter.bidirender import add_bidi_support, render_text
import arabic_reshaper
from bidi.algorithm import get_display
import sys

class ATkEntry(tkinter.Entry):

    def __init__(self, master, placeholder_text,show="",arabic=True, **kwargs):
        tkinter.Entry.__init__(self, master, **kwargs)
        
        
        self.configure(
            #font = 
            foreground="#B0B0B0",
            background="#373737",
            insertbackground="#B0B0B0",
            highlightcolor = "#444444",
            highlightbackground="#444444",
            highlightthickness=1,
            borderwidth=0,
            relief="flat"
        )
        self.show=show
        
        if not sys.platform.startswith('win'):
            add_bidi_support(self)
            
        if arabic:
            self.arabic_placeholder=True
            self.configure(justify="right")
        self.placeholder_text = placeholder_text
        self.isInserted=False
        self.insertPlaceholder()
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.master=master
        
        
    def on_focus_in(self, event):
        if self.isInserted:
            self.changeMode()

    
    def changeMode(self):
        self.delete(0, tkinter.END)
        self.isInserted=False
        self.configure(foreground="#FFFFFF")
        if self.show=="*":
            self.configure(show="*") 
            
    def insertPlaceholder(self):
        if self.arabic_placeholder == True:
            self.insert(0, self.toArabic(self.placeholder_text))
        else:
            self.insert(0, self.placeholder_text)
        self.isInserted=True
    
    def reload(self):
        self.delete(0, tkinter.END)   
        self.configure(foreground="#B0B0B0",show="")  
        self.insertPlaceholder()
        self.master.focus_set()
        
        
    def on_focus_out(self, event):
        if not self.get():
            self.insertPlaceholder()
            self.configure(foreground="#B0B0B0",show="")

            
    def get_text(self):
        text = self.get()
        if self.isInserted:
            return ''
        else:
            return text
            
    def toArabic(self,text):
        if sys.platform.startswith('win'):
            #s = text.split()
            #s.reverse()
            #result = " ".join(s)
            return text
        return get_display(arabic_reshaper.reshape(text))
