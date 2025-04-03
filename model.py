from meter import METER_TYPE

class Model:

    ID = 0

    def __init__(self):
        self.files = {}

    def create(self, file_type: METER_TYPE, date, value):
        file = file_type.value(date, value)
        self.files[self.ID] = file
        self.ID += 1
        return self.ID-1

    def remove(self, id):
        self.files.pop(id)