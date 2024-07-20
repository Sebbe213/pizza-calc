import tkinter as tk

class CreateButton:
    def __init__(self, root, x, y, text, color, command, width, height):
        self.root = root
        self.row = x
        self.column = y
        self.text = text
        self.color = color
        self.command = command
        self.width = width
        self.height = height

    def initiate_button(self):
        btn = tk.Button(self.root, text=self.text, fg=self.color, command=self.command,width= self.width,height=self.height)
        btn.place(x=self.row, y=self.column)
