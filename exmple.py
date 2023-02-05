from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


# calculator example as an introduction to PyQt6 library

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth: DD/MM/YYYY")
        self.date_birth_line_edit = QLineEdit("01/01/1900")

        calculate_button = QPushButton("Calculate")
        self.output_label = QLabel("")

        calculate_button.clicked.connect(self.calculate_age)

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(self.output_label, 2, 0)
        grid.addWidget(calculate_button, 2, 1)

        self.setLayout(grid)

    def calculate_age(self):
        now = datetime.now().date()
        date_of_birth = self.date_birth_line_edit.text()
        date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y').date()
        difference = now - date_of_birth
        difference = int(difference.days/365)
        self.output_label.setText(f"{self.name_line_edit.text()} is {str(difference)} year old right now.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
