from collections import namedtuple
import enum

class Meter:

    PARAMETERS = {"date": str, 'value': int}
    
    def __init__(self, date, val):
        self.date = date
        self.val = val
    
    def print_all(self):
        pass
    

class ColdWaterMeter(Meter):

    TYPE = 'cold_water'
    RUSSIAN_TYPE_NAME = 'Счетчик холодной воды'
    
    def print_all(self):
        print("cold water", self.date, self.val)


class HotWaterMeter(Meter):

    TYPE = 'hot_water'
    RUSSIAN_TYPE_NAME = 'Счетчик горячей воды'
    
    def print_all(self):
        print("hot water", self.date, self.val)


class ElectricityMeter(Meter):

    TYPE = 'electricity'
    RUSSIAN_TYPE_NAME = 'Счетчик электричества'
    
    def print_all(self):
        print(self.type, self.date, self.val)


file_type = namedtuple('FileType', ['file_class'])

class METER_TYPE(enum.Enum):
    COLD_WATER = ColdWaterMeter
    HOT_WATER = HotWaterMeter
    ELECTRICITY = ElectricityMeter

    @staticmethod
    def get_type_on_name(name):
        for i in METER_TYPE._member_map_.values():
            if i.value.TYPE == name or i.value.RUSSIAN_TYPE_NAME == name:
                return i

