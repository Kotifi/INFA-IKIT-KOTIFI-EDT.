import enum

class Meter:

    TYPE = None
    TYPE_NAME = None
    RUSSIAN_TYPE_NAME = None
    PARAMETERS = {"date": str, 'value': int}
    
    def __init__(self, date, val):
        self.date = date
        self.val = val
    
    def print_all(self):
        print(self.RUSSIAN_TYPE_NAME, self.date, self.val)

    def get_params(self):
        return {'type': self.TYPE, 'date': self.date, 'value': self.val}
    

class ColdWaterMeter(Meter):

    TYPE = 'cold_water'
    TYPE_NAME = 'Cold Water'
    RUSSIAN_TYPE_NAME = 'Счетчик холодной воды'


class HotWaterMeter(Meter):

    TYPE = 'hot_water'
    TYPE_NAME = 'Hot Water'
    RUSSIAN_TYPE_NAME = 'Счетчик горячей воды'
    

class ElectricityMeter(Meter):

    TYPE = 'electricity'
    TYPE_NAME = 'Electricity'
    RUSSIAN_TYPE_NAME = 'Счетчик электричества'


class METER_TYPE(enum.Enum):
    COLD_WATER = ColdWaterMeter
    HOT_WATER = HotWaterMeter
    ELECTRICITY = ElectricityMeter

    @staticmethod
    def get_type_on_name(name):
        for i in METER_TYPE._member_map_.values():
            if i.value.TYPE == name or i.value.RUSSIAN_TYPE_NAME == name:
                return i
        return None

