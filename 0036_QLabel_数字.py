from PySide6.QtWidgets import QLabel, QApplication
import sys


class Window(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(480, 720)

        self.setNum(3.14159)

        self.setNum(314159)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
