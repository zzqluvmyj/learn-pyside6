import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIntValidator

"""
void QLineEdit:: setValidator (const QValidator * v )
将行编辑值的验证器设置为v。

只有当v验证行编辑的内容为Acceptable时，才会发出行编辑的returnPressed () 和editingFinished () 信号。用户可以在编辑期间将内容更改为任何中间值，但将无法将文本编辑为v验证为Invalid的值。

这允许您限制在编辑完成时最终应输入的文本，同时让用户有足够的自由将文本从一种有效状态编辑到另一种有效状态。

如果v == 0，setValidator() 删除当前输入验证器。初始设置是没有输入验证器（即接受任何输入直到maxLength ()）。

hasAcceptableInput () 
输入是否满足inputMask和验证器。
默认情况下，此属性为true.

以下以QIntValidator（继承于QValidator）为例来简单说明
TODO 更多内容见QValidator
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.setCentralWidget(self.line_edit)
        self.line_edit.setValidator(QIntValidator(0, 100, self))
        self.line_edit.textChanged.connect(self.text_changed)

    @Slot(str)
    def text_changed(self, s):
        print("text_changed", self.line_edit.hasAcceptableInput())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
