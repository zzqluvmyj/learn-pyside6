from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QApplication
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        # 必须要手动设置大小或者先调用show()，center()方法才能生效
        # 原因：猜测是在show之前，获取到的窗口大小和将要显示的尺寸不相符
        self.center()
        self.show()

    def center(self):
        """屏幕居中方法"""
        screen = QGuiApplication.primaryScreen().size()  # 获取屏幕参数
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    app.exec()
