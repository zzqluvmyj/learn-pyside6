import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        # addWidget(arg__1: QWidget, row: int, column: int, rowSpan: int, columnSpan: int, alignment: Alignment = ...) -> None
        # arg__1就是要添加的小部件
        # row是添加的行
        # column是添加的列
        # rowSpan是表示跨了多少行
        # columnSpan是表示跨了都列
        # alignment是布局，不再细说，具体看0007
        self.layout.addWidget(QLabel("label 1"), 1, 1, 1, 2)
        self.layout.addWidget(QLabel("label 2"), 2, 1, 2, 1)
        self.layout.addWidget(QLabel("label 3"), 2, 2)
        self.layout.addWidget(QLabel("label 4"), 3, 2)


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
