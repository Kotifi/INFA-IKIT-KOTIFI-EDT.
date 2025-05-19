from PySide6.QtWidgets import QCheckBox, QLabel, QHBoxLayout, QWidget
from PySide6 import QtCore


class RowWidget(QWidget):

    selected = QtCore.Signal(bool, int)

    def __init__(self, id, file_type, date, value):

        super().__init__()

        self.setFixedSize(600, 50)
        self.id = id

        self.type_label = QLabel()
        self.type_label.setFixedSize(150, 50)
        self.type_label.setText('<b>' + file_type + '</b>')

        self.date_label = QLabel()
        self.date_label.setFixedSize(150, 50)
        self.date_label.setText(date)

        self.value_label = QLabel()
        self.value_label.setFixedSize(150, 50)
        self.value_label.setText(str(value))

        self.check_box = QCheckBox()
        self.check_box.stateChanged.connect(self.select_row)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.type_label)
        self.central_layout.addWidget(self.date_label)
        self.central_layout.addWidget(self.value_label)
        self.central_layout.addWidget(self.check_box)
        self.setLayout(self.central_layout)
    
    def select_row(self, state):
        if state == 2:
            self.selected.emit(True, self.id)
        else:
            self.selected.emit(False, self.id)
