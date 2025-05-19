<<<<<<< HEAD
from collections import namedtuple
=======
>>>>>>> branch1
import enum

class Meter:

<<<<<<< HEAD

=======
    TYPE = None
    TYPE_NAME = None
    RUSSIAN_TYPE_NAME = None
    PARAMETERS = {"date": str, 'value': int}
>>>>>>> branch1
    
    def __init__(self, date, val):
        self.date = date
        self.val = val
    
    def print_all(self):
<<<<<<< HEAD
        pass
=======
        print(self.RUSSIAN_TYPE_NAME, self.date, self.val)

    def get_params(self):
        return {'type': self.TYPE, 'date': self.date, 'value': self.val}
>>>>>>> branch1
    

class ColdWaterMeter(Meter):

    TYPE = 'cold_water'
<<<<<<< HEAD
    RUSSIAN_TYPE_NAME = 'Счетчик холодной воды'
    
    def print_all(self):
        print("cold water", self.date, self.val)
=======
    TYPE_NAME = 'Cold Water'
    RUSSIAN_TYPE_NAME = 'Счетчик холодной воды'
>>>>>>> branch1


class HotWaterMeter(Meter):

    TYPE = 'hot_water'
<<<<<<< HEAD
    RUSSIAN_TYPE_NAME = 'Счетчик горячей воды'
    
    def print_all(self):
        print("hot water", self.date, self.val)

=======
    TYPE_NAME = 'Hot Water'
    RUSSIAN_TYPE_NAME = 'Счетчик горячей воды'
    
>>>>>>> branch1

class ElectricityMeter(Meter):

    TYPE = 'electricity'
<<<<<<< HEAD
    RUSSIAN_TYPE_NAME = 'Счетчик электричества'
    
    def print_all(self):
        print(self.type, self.date, self.val)


file_type = namedtuple('FileType', ['file_class'])

=======
    TYPE_NAME = 'Electricity'
    RUSSIAN_TYPE_NAME = 'Счетчик электричества'


>>>>>>> branch1
class METER_TYPE(enum.Enum):
    COLD_WATER = ColdWaterMeter
    HOT_WATER = HotWaterMeter
    ELECTRICITY = ElectricityMeter

    @staticmethod
    def get_type_on_name(name):
        for i in METER_TYPE._member_map_.values():
            if i.value.TYPE == name or i.value.RUSSIAN_TYPE_NAME == name:
                return i
<<<<<<< HEAD
=======
        return None
>>>>>>> branch1

