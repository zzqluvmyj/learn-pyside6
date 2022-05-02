from os import stat
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction


# 继承QMainWindow才会有菜单栏
# addAction和addMenu有非常多的重载的函数，使用的时候再挑选，此处不再赘述
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # menuBar()可以添加menu或者action
        self.file_menu = self.menuBar().addMenu("文件")
        self.file_menu.setTitle("所有文件")  # 设置菜单文本
        print(self.file_menu.title())  # 读取菜单文本

        self.open_file_action = QAction("打开", self)  # 创建动作
        self.open_file_action.setShortcut("Ctrl+O")  # 添加快捷键
        self.open_file_action.triggered.connect(
            self.open_file
        )  # 绑定事件,单击任何QAction按钮时，QMenu对象都会发射triggered信号
        self.open_file_action.setText("打开文件")  # 设置动作文本
        print(self.open_file_action.text())  # 读取菜单文本
        self.file_menu.addAction(self.open_file_action)  # 添加动作到菜单栏

        # 一次性添加动作到菜单中
        self.recent_file_menu = self.file_menu.addMenu("最近")
        self.recent_file_menu.addAction("111")
        self.recent_file_menu.addAction("222")

        self.file_menu.addSeparator()  # 添加分隔线

        # 一次性添加动作到菜单中
        self.file_menu.addAction("退出", "Ctrl+Q", QApplication.instance().quit)

        # 禁用菜单
        self.no_use_action = self.menuBar().addAction("不可用")
        self.no_use_action.setEnabled(True)

        # 勾选菜单
        self.check_action = QAction("勾选", self)
        self.check_action.setCheckable(True)  # 设置勾选菜单
        self.check_action.setChecked(True)  # 设置已勾选
        self.check_action.triggered.connect(self.check_menu)  # 连接插槽
        self.file_menu.addAction(self.check_action)

        # self.menuBar().clear()  # 删除菜单栏内容

        # 注意：如果需要多级菜单，则添加QMenu而不是QAction，QMenu在PySide6.QtWidgets而QAction在PySide6.QtGui

    @Slot()
    def open_file(self):
        print("open file")

    @Slot(bool)
    def check_menu(self, state):
        print(state)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.resize(200, 200)
    w.show()
    app.exec()
