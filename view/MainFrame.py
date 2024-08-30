import tkinter as tk
from view import CreateButton as cb
from view import CreateFrame as cf
from view import CreateTextField as ctf
from view import CreateText as ct
from model import Textfieldinserter as tx
from model import DoughCalculation as dc
from view import DisplayResults as dr


def main_frame():

    add_flour = tx.Textfieldinserter()
    add_water = tx.Textfieldinserter()
    add_salt = tx.Textfieldinserter()
    add_time = tx.Textfieldinserter()
    add_people = tx.Textfieldinserter()
    app = cf.CreateFrame(400, 400)
    app.frame("Pizza calculator")
    results= dr.DisplayResults(app.get_root())
    amount_flour = ctf.CreateTextField(app.get_root(),50,50,10,2.49)
    amount_flour.text_field()
    amount_water = ctf.CreateTextField(app.get_root(),50,100,10,2.49)
    amount_water.text_field()
    amount_salt = ctf.CreateTextField(app.get_root(),50,150,10,2.49)
    amount_salt.text_field()
    time = ctf.CreateTextField(app.get_root(),50,200,10,2.49)
    time.text_field()
    people = ctf.CreateTextField(app.get_root(),50,250,10,2.49)
    people.text_field()

    flour_text = ct.CreateText(app.get_root(),"Dough weight",185,55)
    flour_text.create_label()

    water_text = ct.CreateText(app.get_root(),"% Water (0-1)",185,105)
    water_text.create_label()

    salt_text = ct.CreateText(app.get_root(),"% Salt (0-1)",185,155)
    salt_text.create_label()

    time_text= ct.CreateText(app.get_root(),"Fermentation time" ,185,205)
    time_text.create_label()

    people_text = ct.CreateText(app.get_root(), "Amount of doughs", 185,255)
    people_text.create_label()

    add_flour_button = cb.CreateButton(app.get_root(),135,49,"+","black",lambda: add_flour.add_button_pressed(amount_flour.return_text_field()),5,2)
    add_flour_button.initiate_button()
    subtract_flour_button = cb.CreateButton(app.get_root(),5,49,"-","black",lambda: add_flour.subtract_button_pressed(amount_flour.return_text_field()),5,2)
    subtract_flour_button.initiate_button()

    add_water_button = cb.CreateButton(app.get_root(), 135, 100, "+", "black", lambda: add_water.add_button_smal(amount_water.return_text_field()), 5, 2)
    add_water_button.initiate_button()
    subtract_water_button = cb.CreateButton(app.get_root(), 5, 100, "-", "black",lambda: add_water.subtract_button_smal(amount_water.return_text_field()), 5, 2)
    subtract_water_button.initiate_button()

    add_salt_button = cb.CreateButton(app.get_root(), 135, 149, "+", "black",lambda: add_salt.add_button_smal(amount_salt.return_text_field()), 5, 2)
    add_salt_button.initiate_button()
    subtract_salt_button = cb.CreateButton(app.get_root(), 5, 149, "-", "black",lambda: add_salt.subtract_button_smal(amount_salt.return_text_field()), 5, 2)
    subtract_salt_button.initiate_button()

    add_time_button = cb.CreateButton(app.get_root(), 135, 200, "+", "black",lambda: add_time.add_button_pressed(time.return_text_field()), 5, 2)
    add_time_button.initiate_button()
    subtract_time_button = cb.CreateButton(app.get_root(), 5, 200, "-", "black",lambda: add_time.subtract_button_pressed(time.return_text_field()), 5, 2)
    subtract_time_button.initiate_button()

    add_people_button = cb.CreateButton(app.get_root(), 135, 249, "+", "black", lambda: add_people.add_button_pressed(people.return_text_field()), 5, 2)
    add_people_button.initiate_button()
    subtract_people_button = cb.CreateButton(app.get_root(), 5, 249, "-", "black",lambda: add_people.subtract_button_pressed(people.return_text_field()), 5, 2)
    subtract_people_button.initiate_button()

    calculate_button = cb.CreateButton(app.get_root(),300,300,"calculate","black",lambda : results.calculate(people, amount_flour, amount_water, amount_salt, time),10,2)
    calculate_button.initiate_button()
    app.start()