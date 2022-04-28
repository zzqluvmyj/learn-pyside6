import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w1 = QLabel("title")
    w1.setObjectName("title")
    w1.show()

    w2 = QLabel("no title")
    w2.show()

    with open("assets/QLabel.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
