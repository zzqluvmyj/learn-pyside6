import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

# 任意布局之间都可以相互嵌套
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.layout = QHBoxLayout(self)
        self.layout.addLayout(self.vlayout1)  # 增加子布局
        self.layout.addLayout(self.vlayout2)  # 增加子布局

        self.vlayout1.addWidget(QLabel("vlabel 1 1"))
        self.vlayout1.addWidget(QLabel("vlabel 1 2"))

        self.vlayout2.addWidget(QLabel("vlabel 2 1"))
        self.vlayout2.addWidget(QLabel("vlabel 2 2"))

        self.layout.addWidget(QLabel("main label 1"))
        self.layout.addWidget(QLabel("main label 2"))
        self.layout.addWidget(QLabel("main label 3"))


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
