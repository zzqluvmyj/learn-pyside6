# setCompleter

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QCompleter
from PySide6.QtCore import Qt

"""
QCompleter 类提供基于项目模型的完成
可以使用 QCompleter 在任何 Qt 小部件中提供自动完成功能，例如QLineEdit和QComboBox。

TODO 更多内容见QCompleter
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.setCentralWidget(self.line_edit)
        self.c = QCompleter(["1111", "1122", "1233"], self)
        self.line_edit.setCompleter(self.c)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
