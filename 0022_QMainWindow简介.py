import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# QMainWindow类提供一个有菜单条、工具栏、状态条的主应用程序窗口
# 一个主窗口提供了构建应用程序的用户界面框架。Qt拥有QMainWindow及其相关类来管理主窗口。
# QMainWindow拥有自己的布局，我们可以使用QMenuBar（菜单栏）、QToolBar（工具栏）、QStatusBar（状态栏）以及QDockWidget（悬浮窗体），布局有一个可由任何种类小窗口所占据的中心区域。
# QMainWindow并没有setLayout()函数，因此不能使用setLayout()函数来设置layout，需要使用间接的方法。
# 需要做的只是先定义一个QWidget对象，然后使用QMainWindow::setCentralWidget()函数来将该QWidget对象设置为Central Widget，然后使用该QWidget对象的setLayout()函数，就可以了，不过后续对象都要被添加到该QWidget对象下的layout中。
# QMainWindow有一个车默认的layout，具体如下
# https://blog.csdn.net/imred/article/details/54387583
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # QMainWindow中的
        # 状态栏见状态栏
        # 菜单栏见菜单栏
        # 工具栏见工具栏
        # 悬浮窗体见悬浮窗体

        # 设置和获取中心的小部件
        # 如果需要布局，请添加布局小部件
        self.setWindowTitle("QMainWindow")
        print(self.centralWidget())
        self.setCentralWidget(QLabel("hello world"))
        print(self.centralWidget())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
