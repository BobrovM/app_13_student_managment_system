import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit("10")

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit("2")

        self.combo_box = QComboBox()
        self.items_list = ["Metric (km)", "Imperial (miles)"]
        self.combo_box.addItems(self.items_list)

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.combo_box, 2, 0)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        distance = int(self.distance_line_edit.text())
        time = int(self.time_line_edit.text())
        result = round(distance / time, 2)
        if self.combo_box.currentText() == self.items_list[0]:
            self.result_label.setText(f"Average speed is {result} km/h")
        elif self.combo_box.currentText() == self.items_list[1]:
            self.result_label.setText(f"Average speed is {result} mph")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
