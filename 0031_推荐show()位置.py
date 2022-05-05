from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QApplication
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    # show()方法应该放在调用的时候，而不是在__init__方法中
    # 因为有些类可以为顶级窗口、组件或子窗口
    # 如果为顶级窗口，则没有问题
    # 如果是组件或子窗口，则会影响界面逻辑混乱，造成组件或子窗口提前单独显示
    # 类似内容参见0025
    w.show()
    app.exec()
