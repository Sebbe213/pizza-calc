import tkinter as tk
from view import CreateButton as cb
from view import CreateFrame as cf
from view import CreateTextField as ctf
from view import CreateText as ct
from model import Textfieldinserter as tx

def main_frame():
    add = tx.Textfieldinserter()
    app = cf.CreateFrame(400, 400)
    app.frame("Pomodoro timer")
    amount_flour = ctf.CreateTextField(app.get_root(),50,50,10,2.49)
    amount_flour.text_field()
    #flour_text = ct.CreateText(app.get_root(),"flour",155,50)
    #flour_text.create_label()
    add_flour_button = cb.CreateButton(app.get_root(),135,49,"+","black",lambda: add.add_button_pressed(amount_flour.return_text_field()),5,2)
    add_flour_button.initiate_button()
    app.start()