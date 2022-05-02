import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.layout.addWidget(QLabel("label 1"), 1, 1, 1, 2)
        self.layout.addWidget(QLabel("label 2"), 2, 1, 2, 1)
        self.layout.addWidget(QLabel("label 3"), 2, 2)
        self.layout.addWidget(QLabel("label 4"), 3, 2)
        self.layout.setSpacing(20)  # 设置间距为20像素


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
