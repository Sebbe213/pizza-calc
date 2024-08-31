from model import DoughCalculation as dc
from view import CreateText as ct

class DisplayResults:
    def __init__(self,root):
        self.root = root
        self.obj = dc.DoughCalculation()
        self.flour_text = ct.CreateText(self.root, "", 300, 50)
        self.water_text = ct.CreateText(self.root, "", 300, 100)
        self.salt_text = ct.CreateText(self.root, "", 300, 150)
        self.yeast_text = ct.CreateText(self.root, "", 300, 200)
        self.error_text = ct.CreateText(self.root, "You need to fill all text fields!", 300, 50)

    def calculate(self, people, flour, water, salt, time):
        try:
            self.obj.set_total_dough_weight(int(people.get_text()), int(flour.get_text()))
            self.obj.set_total_flour_amount(float(salt.get_text()), float(water.get_text()))
            self.obj.set_yeast_amount(int(time.get_text()))
            self.obj.set_water_amount(float(water.get_text()))
            self.obj.set_salt_amount(float(salt.get_text()))

            self.flour_text.text = f" flour: {str(self.obj.get_total_flour_amount())} grams"
            self.flour_text.create_label()
            self.water_text.text = f"water: {str(self.obj.get_water_amount())} grams"
            self.water_text.create_label()
            self.salt_text.text = f"salt: {str(self.obj.get_salt_amount())} grams"
            self.salt_text.create_label()
            self.yeast_text.text = f"yeast: {str(self.obj.get_yeast_mount())} grams"
            self.yeast_text.create_label()
            self.error_text.text = ""
            self.error_text.create_label()
        except ValueError:
            self.error_text.create_label()


        #yeast_error_text = ct.CreateText(self.root, f"{str(self.obj.get_error_message())}", 300, 200)
        #yeast_error_text.create_label()

        #self.error_message = ct.CreateText(self.root, "", 300, 50)
        #self.error_message.create_label()


