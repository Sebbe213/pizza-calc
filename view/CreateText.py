
import tkinter as tk

class CreateText:
    def __init__(self,root,text,x,y):
        self.lbl = None
        self.root = root
        self.text = text
        self.x = x
        self.y = y


    def create_label(self):
        if self.lbl is not None:
            self.lbl.destroy()
            self.lbl = None
            self.root.update()

        self.lbl = tk.Label(self.root, text=self.text)
        self.lbl.place(x=self.x, y=self.y)

