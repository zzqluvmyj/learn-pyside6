import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
)
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QAction

"""
如果未设置掩码，则 inputMask() 返回一个空字符串。
验证器可以代替掩码使用，也可以与掩码结合使用；参见setValidator ()。
通过传递一个空字符串 ("")取消设置掩码并返回到正常的QLineEdit操作。

输入掩码是输入模板字符串。它可以包含以下元素：
掩码字符	定义在此位置被视为有效的输入字符的类别
元字符	各种特殊含义
分隔符	所有其他字符都被视为不可变的分隔符
具体见 https://doc.qt.io/qt-6/qlineedit.html#inputMask-prop

hasAcceptableInput () 
输入是否满足inputMask和验证器。
默认情况下，此属性为true.
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.setCentralWidget(self.line_edit)
        self.line_edit.setInputMask("9999-99-99")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
