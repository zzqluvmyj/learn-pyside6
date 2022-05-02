import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt


# 继承QMainWindow才会有状态栏
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.statusBar().showMessage("准备就绪")  # 显示临时信息
        # self.statusBar().clearMessage()  # 删除临时信息

        hello_label = QLabel("hello")
        self.statusBar().addWidget(QLabel("hello"))  # 添加小部件
        # self.statusBar().removeWidget(hello_label)  # 删除小部件
        self.statusBar().addPermanentWidget(hello_label)  # 永久添加小部件，添加在右侧
        hello_label.setText("world")

        # 注意
        # 永久小部件和临时信息可以共存
        # 小部件和临时小部件可以共存，但不能是同一个小部件
        # 小部件和临时信息不能共存，两者同时出现时，以临时信息为主


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
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
