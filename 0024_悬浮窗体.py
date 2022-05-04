import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDockWidget
from PySide6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QLabel("center"))  # 设置中心小部件便于查看QDockWidget的相对位置

        self.dock = QDockWidget("悬浮窗", self)  # 创建QDockWidget
        self.dock.setWidget(QLabel("你好"))  # 设置QDockWidget其中的小部件

        # 调整大小
        self.dock.setMinimumWidth(80)
        self.dock.setMinimumHeight(50)

        # 设置QDockWidget可以停靠的位置，如下所示，多种特性按位与
        # LeftDockWidgetArea:左侧停靠区域
        # RightDockWidgetArea:右侧停靠区域
        # TopDockWidgetArea:顶部停靠区域
        # BottomDockWidgetArea:底部停靠区域
        # NoDockWidgetArea:无法停靠

        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # 设置QDockWidget窗口停靠的特性，如下所示，多种特性按位与
        # DockWidgetClosable:可关闭
        # DockWidgetMovable：可移动
        # DockWidgetFloatable：可漂浮
        # DockWidgetVerticalTitleBar：在左边显示垂直的标签栏
        # NoDockWidgetFeatures:无法关闭，不能悬浮，不能移动

        self.dock.setFeatures(
            QDockWidget.DockWidgetClosable
            | QDockWidget.DockWidgetMovable
            | QDockWidget.DockWidgetFloatable
        )
        # self.dock.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        # self.dock.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.addDockWidget(
            Qt.RightDockWidgetArea, self.dock
        )  # 添加QDockWidget到QMainWindow的合适的位置

        self.dock.setFloating(False)  # 设置是否悬浮，默认为否


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.resize(300, 300)
    w.show()
    app.exec()
