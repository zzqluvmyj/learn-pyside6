import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
w = QLabel("<h1>hello world</h1>")
w.show()
w.setAlignment(Qt.AlignCenter)
w.setStyleSheet(
    """
    color: red;
    """
)

app.exec()
