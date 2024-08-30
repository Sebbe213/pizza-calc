import tkinter as tk
class CreateFrame:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root = tk.Tk()


    def frame(self,text):
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title(text)

    def get_root(self):
        return self.root

    def start(self):
        self.root.mainloop()


