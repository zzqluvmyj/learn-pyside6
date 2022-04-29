import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # self.layout = QVBoxLayout(self)
        # 或者
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 弹簧会把多余的空间顶起来
        self.layout.addWidget(QLabel("label 1"))
        self.layout.addStretch(2)  # 增加弹簧，设定系数为2
        self.layout.addWidget(QLabel("label 2"))
        self.layout.addWidget(QLabel("label 3"))
        self.layout.addStretch(1)  # 增加弹簧，设定系数为1
        # 两个弹簧的系数之比就是拉伸时的伸缩量之比


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.resize(200, 200)
    w.show()
    # 设置QLabel的样式边框，便于查看
    app.setStyleSheet(
        """
        QLabel {
            border:1px solid;
        }
    """
    )
    app.exec()
