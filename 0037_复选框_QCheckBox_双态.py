from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QApplication
import sys

"""
QCheckBox 小部件提供了一个带有文本标签的复选框

QCheckBox是一个选项按钮，可以打开（选中）或关闭（未选中）。
复选框通常用于表示应用程序中可以启用或禁用而不影响其他功能的功能,可以实现不同类型的行为。
例如，QButtonGroup可用于对复选按钮进行逻辑分组，允许独占复选框。但是，QButtonGroup不提供任何视觉表示。

每当检查或清除复选框时，它都会发出信号statechanged（）。如果您想在每次复选框更改状态时触发操作，请连接到此信号。您可以使用isChecked () 来查询复选框是否被选中。

除了通常的选中和未选中状态之外，QCheckBox 还可以选择提供第三种状态来指示“没有变化”。当您需要为用户提供既不选中也不取消选中复选框的选项时，这很有用。如果你需要这第三种状态，使用setTristate () 启用它，并使用checkState () 来查询当前的切换状态。

就像QPushButton一样，一个复选框显示文本，以及一个可选的小图标。
图标是用setIcon () 设置的。文本可以在构造函数中设置，也可以用setText () 设置。
可以通过在首选字符前加上 & 符号来指定快捷键。
要显示实际的 & 符号，请使用“&&”。

更多内容见：按钮抽象基类_QAbstractButton
"""


class Window(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 设置复选框文本
        self.setText("书籍")

        # 设置复选框状态
        self.setChecked(True)

        # 是否选中
        print(self.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
