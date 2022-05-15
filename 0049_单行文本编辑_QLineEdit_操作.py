import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
)
from PySide6.QtCore import Qt, QPoint

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.setCentralWidget(self.line_edit)

        self.del_menu = self.menuBar().addMenu("删除")
        self.del_menu.addAction("backspace()", lambda: self.line_edit.backspace())
        self.del_menu.addAction("del_()", lambda: self.line_edit.del_())
        self.del_menu.addAction("clear()", lambda: self.line_edit.clear())

        self.cursor_menu = self.menuBar().addMenu("光标")
        self.cursor_menu.addAction(
            "光标位置移动到1", lambda: self.line_edit.setCursorPosition(1)
        )
        self.cursor_menu.addAction(
            "当前光标位置",
            lambda: self.statusBar().showMessage(str(self.line_edit.cursorPosition())),
        )
        self.cursor_menu.addAction(
            "(10,10)处的光标位置",
            lambda: self.statusBar().showMessage(
                str(self.line_edit.cursorPositionAt(QPoint(10, 10)))
            ),
        )
        self.cursor_menu.addAction(
            "光标向前移动3次",
            lambda: self.line_edit.cursorForward(False, 3),
        )
        self.cursor_menu.addAction(
            "光标向前移动3次并选中",
            lambda: self.line_edit.cursorForward(True, 3),
        )
        self.cursor_menu.addAction(
            "光标向后移动3次",
            lambda: self.line_edit.cursorBackward(False, 3),
        )
        self.cursor_menu.addAction(
            "光标向后移动3次并选中",
            lambda: self.line_edit.cursorBackward(True, 3),
        )
        self.cursor_menu.addAction(
            "光标向前移动一个单词",
            lambda: self.line_edit.cursorWordForward(False),
        )
        self.cursor_menu.addAction(
            "光标向前移动一个单词并选中",
            lambda: self.line_edit.cursorWordForward(True),
        )
        self.cursor_menu.addAction(
            "光标向后移动一个单词",
            lambda: self.line_edit.cursorWordBackward(False),
        )
        self.cursor_menu.addAction(
            "光标向后移动一个单词并选中",
            lambda: self.line_edit.cursorWordBackward(True),
        )
        self.cursor_menu.addAction(
            "行首",
            lambda: self.line_edit.home(False),
        )
        self.cursor_menu.addAction(
            "行首并选中",
            lambda: self.line_edit.home(True),
        )
        self.cursor_menu.addAction(
            "行尾",
            lambda: self.line_edit.end(False),
        )
        self.cursor_menu.addAction(
            "行尾并选中",
            lambda: self.line_edit.end(True),
        )

        self.select_menu = self.menuBar().addMenu("选中")
        self.select_menu.addAction("全选", lambda: self.line_edit.selectAll())
        self.select_menu.addAction("取消选择", lambda: self.line_edit.deselect())
        self.select_menu.addAction(
            "选中文本", lambda: self.statusBar().showMessage(self.line_edit.selectedText())
        )
        self.select_menu.addAction(
            "是否选中",
            lambda: self.statusBar().showMessage(str(self.line_edit.hasSelectedText())),
        )
        self.select_menu.addAction("1-3选中", lambda: self.line_edit.setSelection(1, 3))
        self.select_menu.addAction(
            "选中文本开头索引",
            lambda: self.statusBar().showMessage(str(self.line_edit.selectionStart())),
        )
        self.select_menu.addAction(
            "选中文本结束索引",
            lambda: self.statusBar().showMessage(str(self.line_edit.selectionEnd())),
        )
        self.select_menu.addAction(
            "选中文本长度",
            lambda: self.statusBar().showMessage(str(self.line_edit.selectionLength())),
        )

        self.edit_menu = self.menuBar().addMenu("编辑")
        self.edit_menu.addAction("插入", lambda: self.line_edit.insert("fuck"))
        self.edit_menu.addAction("复制选中文本到剪贴板", lambda: self.line_edit.copy())
        self.edit_menu.addAction("剪切选中文本到剪贴板", lambda: self.line_edit.cut())
        # 将所选文本复制到剪贴板并将其删除（如果有），并且如果echoMode () 为Normal。
        # 如果当前验证器不允许删除选定的文本，cut() 将复制而不删除。
        self.edit_menu.addAction("粘贴剪贴板文本", lambda: self.line_edit.paste())
        # 在光标位置插入剪贴板的文本，删除任何选定的文本，前提是行编辑不是只读的。
        # 如果最终结果对当前验证器无效，则不会发生任何事情。
        self.edit_menu.addAction(
            "设置欢迎文本", lambda: self.line_edit.setText("hello world")
        )
        self.edit_menu.addAction("撤销", lambda: self.line_edit.undo())
        self.edit_menu.addAction("重做", lambda: self.line_edit.redo())

        self.other_menu = self.menuBar().addMenu("其他")
        self.other_menu.addAction(
            "是否修改过",
            lambda: self.statusBar().showMessage(str(self.line_edit.isModified())),
        )
        self.other_menu.addAction(
            "设置修改过",
            lambda: self.line_edit.setModified(True),
        )
        # isModified()可以知道是否修改，进而可以用来辅助设置默认值
        self.other_menu.addAction(
            "是否可以撤销",
            lambda: self.statusBar().showMessage(str(self.line_edit.isUndoAvailable())),
        )
        self.other_menu.addAction(
            "是否可以重做",
            lambda: self.statusBar().showMessage(str(self.line_edit.isRedoAvailable())),
        )
        self.other_menu.addAction(
            "显示文本",
            lambda: self.statusBar().showMessage(str(self.line_edit.displayText())),
        )
        # displayText()保存显示的文本。
        # 如果echoMode为Normal，则返回与text () 相同的值；
        # 如果EchoMode是Password或PasswordEchoOnEdit它返回一个平台相关的密码掩码字符串text ().length() 大小，例如“******”；
        # 如果EchoMode为NoEcho ，则返回一个空字符串“”。
        # 默认情况下，此属性包含一个空字符串。


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
