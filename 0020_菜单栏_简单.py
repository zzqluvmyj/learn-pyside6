import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction


# 继承QMainWindow才会有菜单栏
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # menuBar()可以添加menu或者action
        self.menu = self.menuBar()  # 返回主窗口的QMenuBar对象
        self.file_menu = self.menu.addMenu("文件")  # 添加菜单项
        self.open_file_action = QAction("打开", self)  # 创建动作
        self.file_menu.addAction(self.open_file_action)  # 添加动作
        self.menu.addAction("欢迎", lambda: print("hello"))  # 在menuBar上面添加动作


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.resize(200, 200)
    w.show()
    app.exec()
