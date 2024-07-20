
class DoughCalculation:

    def __init__(self):
        self.total = None
        self.yeast = None
        self.size = None
        self.hydration = None
        self.saltpercentage = None
        self.flour = None
        self.temp = None
        self.water = None
        self.salt = None
        self.yeast = None
        self.time = None


    def set_total_dough_weight(self,amount,size):
        self.size = size
        self.total = amount * self.size

    def get_total_dough_weight(self):
        return self.total

    def set_total_flour_amount(self,salt,water):
        self.hydration = water
        self.saltpercentage = salt
        self.flour = self.size/(1+self.hydration+self.saltpercentage)

    def get_total_flour_amount(self):
        return self.flour

    def set_water_amount(self):
        self.water = self.flour * self.hydration

    def get_water_amount(self):
        return self.water

    def set_salt_amount(self):
        self.salt = self.flour * self.saltpercentage

    def get_salt_amount(self):
        return self.salt

    def set_yeast_amount(self,time):
        self.time = time
        if(self.time >= 8 and self.time <= 12):
            self.yeast = self.flour * 0.0035
        elif(self.time>12 and self.time <=48):
            self.yeast = self.flour * 0.0013
        elif(self.time>48  and self.time<=72):
            self.yeast = self.flour * 0.007
        else:
            self.yeast = "The fermentation time is to long, max should be 72h"

    def get_yeast_mount(self):
        return self.yeast









