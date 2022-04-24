import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout


class Form(QDialog):
    def __init__(self, parent=None):
        # super(Form, self).__init__(parent)
        super().__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")
        self.button.clicked.connect(self.greetings)
        self.setWindowTitle("My Form")
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

    def greetings(self):
        print(f"Hello {self.edit.text()}")


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
