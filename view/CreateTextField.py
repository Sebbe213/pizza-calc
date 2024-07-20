import tkinter as tk
from view import CreateFrame as cf

class CreateTextField:
    def __init__(self,root,x,y,width,height):
        self.root = root
        self.width  = width
        self.height = height
        self.x = x
        self.y = y
        #self.txt = tk.Entry(self.root,width=self.width)

    def text_field(self):
       self.txt = tk.Text(self.root,width=self.width,height=self.height)
       self.txt.place(x=self.x,y=self.y)

    def add_txt(self,text):
        self.txt.insert(0,text)


    def get_text(self):
        return self.txt.get(0,tk.END)

    def return_text_field(self):
        return self.txt