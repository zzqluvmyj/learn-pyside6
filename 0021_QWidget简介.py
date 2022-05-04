import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import (
    QSize,
    QRect,
    QPoint,
)  # 以上三个是pyside6内置的一些数据结构，帮助编写易于维护且条理清晰的诚程序

# 基础窗口控件QWiget类是所有用户界面对象的基类，所有的窗口和小部件都是直接或者间接继承自QWiget类。
# 窗口部件是用户界面的一个原子：它从窗口系统接收鼠标、键盘和其它事件，并且将自己的表现形式绘制在屏幕上。每一个窗口部件都是矩形，并且它们按Z轴顺序排列。一个窗口部件可以被它的父窗口部件或者它前面的窗口部件盖住一部分。
# QWidget有很多成员函数，但是它们中的一些有少量的直接功能：例如，QWidget有字体属性，但是自己从来不用。为很多继承它的子类提供了实际的功能，比如QLabel、QPushButton、QCheckBox等等。
# 没有父窗体的小部件始终是一个独立的窗口（顶级窗口部件）。非窗口的小部件为子部件，它们在父窗口中显示。Qt中大多数部件主要被用作子部件。例如：可以显示一个按钮作为顶层窗口，但大多数人更喜欢将按钮内置于其它部件，如QDialog。
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # 屏幕左上角为(0,0)，从左到右横坐标为X轴，从上到下竖坐标为Y轴。

        self.setGeometry(QRect(100, 100, 200, 200))  # 分别设置窗口左上角定点和窗口大小
        # 或者
        # self.setGeometry(100, 100, 200, 200)
        print(self.x(), self.y(), self.width(), self.height())
        print(self.frameGeometry())

        self.resize(QSize(300, 300))  # 重新设置窗口大小
        # 或者
        # self.resize(300, 300)

        self.setFixedWidth(100)  # 设置固定的宽度
        self.setFixedHeight(300)  # 设置固定的高度
        self.setFixedSize(QSize(100, 300))  # 设置固定的窗口大小
        # 或者
        # self.setFixedSize(100, 300)

        self.move(QPoint(300, 300))  # 移动窗口位置
        # 或者
        self.move(300, 300)
        print(self.pos())  # 窗口左上角位置

        self.setToolTip("这是一个<b>提示信息</b>")  # 设置提示信息


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    app.exec()
