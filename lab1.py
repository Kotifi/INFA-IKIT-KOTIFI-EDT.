
class Meter:
    
    def __init__(self, date, val):
        self.date = date
        self.val = val
    
    def print_all(self):
        pass
    

class ColdWaterMeter(Meter):

    def __init__(self, date, val):
        super().__init__(date, val)
        self.type = 'cold_water'
    
    def print_all(self):
        print("cold water", self.date, self.val)


class HotWaterMeter(Meter):
    
    def __init__(self, date, val):
        super().__init__(date, val)
        self.type = 'hot_water'
    
    def print_all(self):
        print("hot water", self.date, self.val)


class ElectricityMeter(Meter):
    
    def __init__(self, date, val):
        super().__init__(date, val)
        self.type = 'electricity'
    
    def print_all(self):
        print(self.type, self.date, self.val)




arr = []
f = open('1.txt', 'r')
for i in f:
    parameters = i.split()
    if parameters[0] == 'cold_water':
        arr.append(ColdWaterMeter(*parameters[1:]))
    if parameters[0] == 'hot_water':
        arr.append(HotWaterMeter(*parameters[1:]))
    if parameters[0] == 'electricity':
        arr.append(ElectricityMeter(*parameters[1:]))
f.close()

for i in arr:
    i.print_all()
