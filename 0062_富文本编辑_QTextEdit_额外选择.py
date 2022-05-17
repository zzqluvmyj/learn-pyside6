import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtGui import QTextCharFormat, QColor

"""
QTextCursor	cursor
QTextCharFormat	format

setExtraSelections (const QList<QTextEdit::ExtraSelection> & selections )
此功能允许使用给定颜色临时标记文档中的某些区域，指定为selections。
例如，这在编程编辑器中很有用，可以用给定的背景颜色标记整行文本以指示断点的存在

参考自 https://programtalk.com/python-examples/PyQt5.QtWidgets.QTextEdit.ExtraSelection/
TODO 具体原理暂不清楚，以后详细学习QTextCursor和QTextCharFormat再说
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.menu = self.menuBar().addMenu("菜单")
        self.menu.addAction("高亮当前行", lambda: self.highlightCurrentLine())

    def highlightCurrentLine(self):
        selection = QTextEdit.ExtraSelection()
        # foramt即QTextCharFormat实例
        selection.format.setBackground(QColor("red"))
        selection.format.setProperty(QTextCharFormat.FullWidthSelection, True)
        # cursor即QTextCursor实例
        selection.cursor = self.text_edit.textCursor()
        selection.cursor.clearSelection()
        self.text_edit.setExtraSelections([selection])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
