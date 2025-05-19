import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt, Slot
from meter import METER_TYPE
import row_widget


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.rows_widgets = {}
        self.selected_rows = []

        self.setWindowTitle("Таблица файлов")
        self.menu_layout = QVBoxLayout()

        self.setMinimumSize(800, 500)

        self.meter_type_combo_box = QComboBox()
        for i in METER_TYPE._member_map_.values():
            self.meter_type_combo_box.addItem(i.value.RUSSIAN_TYPE_NAME)
        self.create_button = QPushButton()
        self.create_button.setText('Создать')
        self.remove_button = QPushButton()
        self.remove_button.setText('Удалить')
        self.load_button = QPushButton()
        self.load_button.setText('Загрузить из файла')

        self.menu_layout.addWidget(self.meter_type_combo_box)
        self.menu_layout.addWidget(self.create_button)
        self.menu_layout.addWidget(self.remove_button)
        self.menu_layout.addWidget(self.load_button)
        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        self.table_layout = QVBoxLayout()
        self.table_widget = QWidget()
        self.table_widget.setLayout(self.table_layout)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.table_widget)


        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.menu_widget)
        self.central_layout.addWidget(self.scroll)
        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
    
    def get_create_file_type(self):
        type_text = self.meter_type_combo_box.currentText()
        return METER_TYPE.get_type_on_name(type_text)
    
    def add_row(self, id, meter_type, date, value):
        new_row = row_widget.RowWidget(id, meter_type, date, value)
        new_row.selected.connect(self.select_row)
        self.rows_widgets[id] = new_row
        self.table_layout.addWidget(self.rows_widgets[id])

    @Slot(bool, int)
    def select_row(self, state, id):
        if state:
            self.selected_rows.append(id)
        else:
            self.selected_rows.remove(id)
    
    def remove_row(self, id):
        row = self.rows_widgets[id]
        row.deleteLater()
        if id in self.selected_rows:
            self.selected_rows.remove(id)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    m.add_row(1, 'sdf', 'sdf', 'sdsf', 'sdf')
    sys.exit(app.exec())
