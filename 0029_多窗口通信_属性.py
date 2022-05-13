from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QLabel,
)
import sys

# 多窗口通信方式1：通过访问小部件的属性
# 注意：网上可以搜到的示例中，子窗口多为继承于QDialog，此处继承于QLineEdit，本质上没有太多不同
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")

        self.sub_window = SubWindow()  # 让子窗口成为主窗口的一个变量，就不会垃圾回收，窗口就不会一闪而过
        self.sub_window.textChanged.connect(
            lambda s: self.label.setText(self.sub_window.text())
        )  # 当编辑框文本改变时，将会调用该函数，获取到sub_window的属性值并修改label

        self.main = QWidget(self)
        self.setCentralWidget(self.main)

        self.main_layout = QVBoxLayout(self.main)
        self.button = QPushButton("弹窗", self.main)
        self.label = QLabel(self.main)

        self.button.clicked.connect(
            lambda: self.sub_window.show()
        )  # 前面已经创建了子窗口，现在只需要让子窗口显示出来

        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.label)


class SubWindow(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("子窗口")
        self.setWindowModality(Qt.ApplicationModal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
