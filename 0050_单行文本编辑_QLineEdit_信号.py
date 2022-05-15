import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction

"""
void	cursorPositionChanged(int oldPos, int newPos)
移动光标发出该信号

void	editingFinished()
当按下 Return 或 Enter 键时，或者如果行编辑失去焦点并且自上次发出此信号以来其内容已更改，则会发出此信号。
请注意，如果在行编辑上设置了验证器或输入掩码并按下了回车键，
则只有在输入符合输入掩码且验证器返回QValidator::Acceptable时才会发出editingFinished信号。

void	inputRejected()
当用户按下不被认为是可接受输入的键时，会发出此信号。例如，如果按键导致验证器的 validate() 调用返回 Invalid。另一种情况是尝试输入超出行编辑最大长度的更多字符。
注意：在部分文本被接受但不是全部被接受的情况下，仍然会发出此信号。例如，如果设置了最大长度，并且剪贴板文本在粘贴时比最大长度长

void	returnPressed()
该信号在按下 Return 或 Enter 键时发出。请注意，
如果在行编辑上设置了验证器或输入掩码，则仅当输入符合输入掩码并且验证器() 返回QValidator::Acceptable时才会发出 returnPressed() 信号。

void	selectionChanged()
选择改变时发出该信号

void	textChanged(const QString &text)
文本改变发出该信号
与textEdited () 不同，当以编程方式更改文本时也会发出此信号，例如，通过调用setText ()。

void	textEdited(const QString &text)
文本编辑时发出该信号
与textChanged () 不同的是，当以编程方式更改文本时（例如，通过调用setText ()）不会发出此信号。
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.setCentralWidget(self.line_edit)

        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.inputRejected.connect(self.input_rejected)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        self.line_edit.setText("hello QLineEdit")
        # setText以触发text_changed

    @Slot(int, int)
    def cursor_position_changed(self, old_pos, new_pos):
        print("cursor_position_changed", old_pos, new_pos)

    @Slot()
    def editing_finished(self):
        print("editing_finished")

    @Slot()
    def input_rejected(self):
        print("input_rejected")

    @Slot()
    def return_pressed(self):
        print("return_pressed")

    @Slot()
    def selection_changed(self):
        print("selection_changed")

    @Slot(str)
    def text_changed(self, s):
        print("text_changed", s)

    @Slot(str)
    def text_edited(self, s):
        print("text_edited", s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
