from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QApplication
import sys

"""
有关富文本的定义，参见https://doc.qt.io/qt-6/richtext-html-subset.html

此处不做详细展示
"""


class Window(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(480, 720)

        self.setText(
            """<a href="/home">链接</a> <br> <img src="./assets/song.jpg" width="480" height="720">"""
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
