import meter
import sys
from main_window import MainWindow
from model import Model
import create_file_window
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog


class MainController:

    CREATE_WINDOW_CLASS = {meter.METER_TYPE.COLD_WATER: create_file_window.CreateColdWaterMeterWindow, 
                           meter.METER_TYPE.HOT_WATER: create_file_window.CreateHotWaterMeterWindow,
                           meter.METER_TYPE.ELECTRICITY: create_file_window.CreateElectricityMeterWindow}

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.main_window.create_button.clicked.connect(self.view_create_window)
        self.main_window.remove_button.clicked.connect(self.remove_elements)
        self.main_window.load_button.clicked.connect(self.load_elements)
        self.db = Model()
    
    def view_create_window(self):
        self.file_type = self.main_window.get_create_file_type()
        self.create_window = self.CREATE_WINDOW_CLASS[self.file_type]()
        self.create_window.create_button.clicked.connect(self.create)
        self.create_window.show()
    
    def create(self):
        meter_type = self.create_window.get_meter_type()
        parameters = self.create_window.get_parameters()
        id = self.db.create(meter_type, **parameters)
        self.main_window.add_row(id, meter_type.value.TYPE, parameters['date'], parameters['value'])
        self.create_window.close()
        del self.create_window

    def remove_elements(self):
        selected_rows = self.main_window.selected_rows.copy()
        for id in selected_rows:
            self.remove_element(id)

    def remove_element(self, id):
        self.main_window.remove_row(id)
        self.db.remove(id)

    def load_elements(self):
        path = QFileDialog.getOpenFileName()
        path = path[0]
        if path.endswith('.txt'):
            with open(path) as f:
                for meter_element in f:
                    meter_type_name, date, value = meter_element.split(" ")
                    meter_type = meter.METER_TYPE.get_type_on_name(meter_type_name)
                    id = self.db.create(meter_type, date, value)
                    self.main_window.add_row(id, meter_type.value.TYPE, date, value)
    
    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())


if __name__ == '__main__':
    m = MainController()
    m.run()