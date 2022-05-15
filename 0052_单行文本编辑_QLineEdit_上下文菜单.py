# setCompleter

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMenu
from PySide6.QtCore import Qt

"""
void QLineEdit::contextMenuEvent(QContextMenuEvent *event)
Reimplements: QWidget::contextMenuEvent(QContextMenuEvent *event).

Shows the standard context menu created with createStandardContextMenu().

If you do not want the line edit to have a context menu, 
you can set its contextMenuPolicy to Qt::NoContextMenu. 

If you want to customize the context menu, reimplement this function. 

If you want to extend the standard context menu, reimplement this function,
call createStandardContextMenu() and extend the menu returned.

The event parameter is used to obtain the position where the mouse cursor was when the event was generated.
"""


class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    # 重新实现QLineEdit的上下文菜单
    def contextMenuEvent(self, event):
        file_menu = self.createStandardContextMenu()
        # 调用createStandardContextMenu后可以扩展原有的上下文菜单
        # 如果不需要原有的上下文菜单，直接QMenu即可
        new_file_action = file_menu.addAction("新建")
        open_file_action = file_menu.addAction("打开")
        quit_action = file_menu.addAction("退出")
        # 这是上下文菜单的关键
        file_menu.exec(event.globalPos())


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = MyLineEdit(self)
        self.setCentralWidget(self.line_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
