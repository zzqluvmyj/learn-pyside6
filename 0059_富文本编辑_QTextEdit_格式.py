import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCharFormat


"""
QTextCharFormat QTextEdit:: currentCharFormat () const
获取当前格式

void QTextEdit:: setCurrentCharFormat (const QTextCharFormat & format )
通过在编辑器光标上调用QTextCursor::setCharFormat ()来设置插入新文本时使用的字符格式。
如果编辑器有选择，则格式直接应用于选择。

void QTextEdit:: mergeCurrentCharFormat (const QTextCharFormat & modifier )
通过在编辑器光标上调用QTextCursor::mergeCharFormat将修饰符中指定的属性合并为当前字符格式。
如果编辑器有选择，那么修饰符的属性将直接应用于选择。

更多见 QTextCharFormat
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.menu = self.menuBar().addMenu("菜单")
        self.menu.addAction("当前格式为", lambda: print(self.text_edit.currentCharFormat()))
        self.menu.addAction(
            "设置当前格式为楷体",
            lambda: self.text_edit.setCurrentCharFormat(self.format1()),
        )
        self.menu.addAction(
            "将斜体合并到当前格式",
            lambda: self.text_edit.mergeCurrentCharFormat(self.format2()),
        )

        self.text_edit.currentCharFormatChanged.connect(
            self.current_char_format_changed
        )

    @Slot(QTextCharFormat)
    def current_char_format_changed(self, f: QTextCharFormat) -> None:
        print("current_char_format_changed", f)

    def format1(self) -> QTextCharFormat:
        f = QTextCharFormat()
        f.setFont("楷体")
        return f

    def format2(self) -> QTextCharFormat:
        f = QTextCharFormat()
        f.setFontItalic(True)
        return f


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
