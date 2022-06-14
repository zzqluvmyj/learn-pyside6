# setCompleter

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QCompleter,
    QWidget,
    QLabel,
    QVBoxLayout,
)
from PySide6.QtCore import Qt

"""
QCompleter 类提供基于项目模型的完成
可以使用 QCompleter 在任何 Qt 小部件中提供自动完成功能，例如QLineEdit和QComboBox。

TODO 更多内容见QCompleter
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = QWidget(self)
        self.line_edit = QLineEdit(self.w)
        # 多套一个外部的widget是为了更好观察自动完成的视图情况

        self.setCentralWidget(self.w)
        self.c = QCompleter(
            ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"],
            self,
        )
        self.line_edit.setCompleter(self.c)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
