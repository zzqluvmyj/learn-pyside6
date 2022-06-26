from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QApplication
import sys


class Window(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 设置复选框文本
        self.setText("书籍")

        # 设置为三态复选框
        self.setTristate()
        print(self.isTristate())

        # 设置三态复选框的状态
        # Qt.Checked	2	组件被选中
        # Qt.PartiallyChecked	1	组件被半选中
        # Qt.Unchecked	0	组件没有被选中（默认）
        self.setCheckState(Qt.PartiallyChecked)
        print(self.isChecked())  # 半选中也是选中


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
