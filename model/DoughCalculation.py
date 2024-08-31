
class DoughCalculation:

    def __init__(self):
        self.total = 0
        self.yeast = 0
        self.size = 0
        self.hydration = 0
        self.saltpercentage = 0
        self.flour = 0
        self.temp = 0
        self.water = 0
        self.salt = 0
        self.yeast = 0
        self.time = 0
        self.error = 0


    def set_total_dough_weight(self,amount,size):
        self.size = int(size)
        self.total = int(amount) * self.size

    def get_total_dough_weight(self):
        return self.total

    def set_total_flour_amount(self,salt,water):
        self.hydration = float(water)
        self.saltpercentage = float(salt)
        self.flour = self.total/(1+self.hydration+self.saltpercentage)

    def get_total_flour_amount(self):
        return int(self.flour)

    def set_water_amount(self,hydration):
        self.hydration = float(hydration)
        self.water = self.flour * self.hydration

    def get_water_amount(self):
        return int(self.water)

    def set_salt_amount(self,salt):
        self.saltpercentage = float(salt)
        self.salt = self.flour * self.saltpercentage

    def get_salt_amount(self):
        return int(self.salt)

    def set_yeast_amount(self,time):
        self.time = int(time)
        if(self.time >= 8 and self.time <= 12):
            self.yeast = self.flour * 0.0035
        elif(self.time>12 and self.time <=48):
            self.yeast = self.flour * 0.0013
        elif(self.time>48  and self.time<=72):
            self.yeast = self.flour * 0.007
        else:
            self.yeast = "The fermentation is either to long or short needs to be between 8-72h"

    def get_yeast_mount(self):
        return f'{self.yeast:.2f}'
    #def get_error_message(self):
        #return self.error

#add a reste method to reset all the variables







