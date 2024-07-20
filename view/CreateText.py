
import tkinter as tk

class CreateText:
    def __init__(self,root,text,x,y):
        self.root = root
        self.text = text
        self.x = x
        self.y = y

    def create_label(self):
        lbl = tk.Label(self.root,text=self.text)
        lbl.place(x=self.x,y=self.y)

