import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QLabel("Hello World!")
    w.show()
    w.setAlignment(Qt.AlignCenter)
    w.setStyleSheet(
        """
        background-color: #262626;
        color: #FFFFFF;
        font-size: 18px;
        """
    )

    app.exec()
