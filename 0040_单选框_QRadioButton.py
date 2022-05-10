from PySide6.QtCore import Qt
from PySide6.QtWidgets import QRadioButton, QApplication, QWidget, QHBoxLayout
import sys

"""
QRadioButton 小部件提供带有文本标签的单选按钮

RadioButton是一个选项按钮，可以打开（选中）或关闭（未选中）。单选按钮通常会为用户提供“多选一”的选择。在一组单选按钮中，一次只能选中一个单选按钮；如果用户选择另一个按钮，则先前选择的按钮将关闭。

默认情况下，单选按钮是自动排他的。如果启用了自动排他，则属于同一父窗口小部件的单选按钮的行为就像它们是同一排他按钮组的一部分一样。如果您需要属于同一个父窗口小部件的单选按钮的多个独占按钮组，请将它们放入QButtonGroup.

每当打开或关闭按钮时，它都会发出toggled()信号。如果您想在每次按钮更改状态时触发操作，请连接到此信号。isChecked()用于查看是否选择了特定按钮。

就像 一样QPushButton，单选按钮显示文本，以及可选的小图标。图标设置用setIcon()。文本可以在构造函数中设置，也可以使用setText(). 可以通过在文本中在首选字符前加上 & 符号来指定快捷键。

更多内容见：按钮抽象基类_QAbstractButton
"""


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout(self)

        self.button1 = QRadioButton("苹果", self)
        self.button2 = QRadioButton("石榴", self)
        self.button3 = QRadioButton("香蕉", self)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        # 信号连接槽
        self.button1.toggled.connect(self.toggle_button(self.button1.text()))
        self.button2.toggled.connect(self.toggle_button(self.button2.text()))
        self.button3.toggled.connect(self.toggle_button(self.button3.text()))

        # 设置勾选状态
        self.button1.setChecked(True)

    def toggle_button(self, button_text):
        def toggle_button_(state):
            print(button_text, state)
            # 查看是否勾选
            print(
                self.button1.isChecked(),
                self.button2.isChecked(),
                self.button3.isChecked(),
            )

        return toggle_button_


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
