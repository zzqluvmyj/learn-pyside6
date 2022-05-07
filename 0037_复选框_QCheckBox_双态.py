from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QApplication
import sys

"""
QCheckBox是一个选项按钮，可以打开（选中）或关闭（未选中）。
复选框通常用于表示应用程序中可以启用或禁用而不影响其他功能的功能,可以实现不同类型的行为。
例如，QButtonGroup可用于对复选按钮进行逻辑分组，允许独占复选框。但是，QButtonGroup不提供任何视觉表示。
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
