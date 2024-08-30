import decimal
import tkinter as tk
from view import CreateButton as cb

class Textfieldinserter:

    def __init__(self):
        self.i = 0
        self.result = None


    def add_button_pressed(self,text_field):
        self.i+=1
        text_field.delete("1.0",tk.END)
        text_field.insert("1.0",int(self.i))


    def subtract_button_pressed(self,text_field):
        if(self.i>0):
            self.i-=1
            text_field.delete("1.0", tk.END)
            text_field.insert("1.0", int(self.i))
    def add_button_smal(self,text_field):
        if(self.i<=1):
            self.i += 0.05
            text_field.delete("1.0",tk.END)
            text_field.insert("1.0",self.i)
    def subtract_button_smal(self,text_field):
        if (self.i > 0):
            self.i -= 0.05
            text_field.delete("1.0", tk.END)
            text_field.insert("1.0", float(self.i))


    def get_result(self):
        return self.i