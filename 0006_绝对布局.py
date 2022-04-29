import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 200)  # 设置相对位置和大小，相对位置是左上角的点
        self.l1 = QLabel("label 1", self)  # 第二个参数时QLabel的parent父组件
        self.l1.move(10, 10)  # 移动到相对位置
        self.l2 = QLabel("label 2", self)
        QLabel()
        self.l2.setGeometry(100, 100, 50, 50)  # 设置相对位置和大小


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
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
