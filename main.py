from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, \
    QVBoxLayout, QLineEdit, QComboBox, QPushButton
from PyQt6.QtGui import QAction
import sys
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert_student)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        data = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert_student(self):
        dialog = InsertStudentDialog()
        dialog.exec()


class InsertStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name_edit = QLineEdit()
        self.student_name_edit.setPlaceholderText("Student's name")
        layout.addWidget(self.student_name_edit)

        self.course_combo = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_combo.addItems(courses)
        layout.addWidget(self.course_combo)

        self.mobile_edit = QLineEdit()
        self.mobile_edit.setPlaceholderText("Mobile phone number")
        layout.addWidget(self.mobile_edit)

        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name_edit.text()
        course = self.course_combo.itemText(self.course_combo.currentIndex())
        mobile = self.mobile_edit.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
