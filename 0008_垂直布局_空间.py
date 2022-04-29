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

        self.layout.addWidget(QLabel("label 1"))
        self.layout.addSpacing(20)  # 增加空间，定死的空间
        self.layout.addWidget(QLabel("label 2"))

        self.layout.addWidget(QLabel("label 3"))


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
