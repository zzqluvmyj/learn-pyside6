from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QCheckBox, QApplication
import sys


class Window(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 设置复选框文本
        self.setText("书籍")

        # 设置为三态复选框
        self.setTristate()

        # 连接事件
        self.stateChanged.connect(self.state_changed)

    @Slot(int)
    def state_changed(self, state):
        # 此处返回的是改变后的状态
        print(state)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
