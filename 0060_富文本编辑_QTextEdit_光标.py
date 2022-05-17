import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtCore import  QPoint
from PySide6.QtGui import  QTextCursor

"""
QTextCursor cursorForPosition(const QPoint &pos) const
在位置pos（在视口坐标中）返回一个QTextCursor 。

QRect	cursorRect(const QTextCursor &cursor) const
返回一个包含光标的矩形（在视口坐标中）

QRect	cursorRect() const
返回一个包含文本编辑光标的矩形（在视口坐标中）

void	moveCursor(QTextCursor::MoveOperation operation, QTextCursor::MoveMode mode = QTextCursor::MoveAnchor)
通过执行给定的操作移动光标。
如果mode是QTextCursor::KeepAnchor，则光标选择它移动的文本。
这与用户在按住 Shift 键并使用光标键移动光标时达到的效果相同。

TODO 更多见 QTextCursor
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.menu = self.menuBar().addMenu("菜单")
        self.menu.addAction("包含文本编辑光标的矩形", lambda: print(self.text_edit.cursorRect()))
        self.menu.addAction(
            "包含(10,10)处的文本光标对象的矩形",
            lambda: print(
                self.text_edit.cursorRect(
                    self.text_edit.cursorForPosition(QPoint(10, 10))
                )
            ),
        )
        self.menu.addAction(
            "(10,10)处的文本光标对象",
            lambda: print(self.text_edit.cursorForPosition(QPoint(10, 10))),
        )
        self.menu.addAction(
            "光标移动到行首",
            lambda: self.text_edit.moveCursor(QTextCursor.StartOfLine),
        )
        self.menu.addAction(
            "光标移动到行尾",
            lambda: self.text_edit.moveCursor(QTextCursor.EndOfLine),
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
