import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QSpinBox, QScrollArea, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from meter import METER_TYPE

class CreateMeterWindow(QMainWindow):

    TYPE: METER_TYPE

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Создать счетчик")
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()

        self.setMinimumSize(300, 300)

        self.parameters = {}

        l_date = QLabel()
        l_date.setText('Дата')
        w = QLineEdit()
        self.parameters['date'] = w

        self.central_layout.addWidget(l_date)
        self.central_layout.addWidget(w)

        l_value = QLabel()
        l_value.setText('Значение счетчика')
        w = QSpinBox()
        self.parameters['value'] = w

        self.central_layout.addWidget(l_value)
        self.central_layout.addWidget(w)

        self.create_button = QPushButton()
        self.create_button.setText('Создать')

        self.central_layout.addWidget(self.create_button)
        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
    
    def get_meter_type(self):
        return self.TYPE
    
    def get_parameters(self):
        parameters = {}
        for i, v in self.parameters.items():
            if isinstance(v, QLineEdit):
                parameters[i] = v.text()
            elif isinstance(v, QSpinBox):
                parameters[i] = v.value()
        return parameters

class CreateColdWaterMeterWindow(CreateMeterWindow):

    TYPE = METER_TYPE.COLD_WATER

class CreateHotWaterMeterWindow(CreateMeterWindow):

    TYPE = METER_TYPE.HOT_WATER

class CreateElectricityMeterWindow(CreateMeterWindow):

    TYPE = METER_TYPE.ELECTRICITY


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = CreateHotWaterMeterWindow()
    m.show()
    sys.exit(app.exec())