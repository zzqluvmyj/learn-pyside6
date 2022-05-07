from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QApplication
import sys


class Window(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(480, 720)

        # 设置标签图片
        self.setPixmap(QPixmap("./assets/song.jpg"))

        # 是否填充图片
        self.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
