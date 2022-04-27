import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot

# qt和python之间的事件通信是通过信号和插槽来实现的，信号相当于事件，插槽相当于处理该事件的方法
# 信号和插槽绑定后，触发了事件，插槽的方法才会执行


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.click)
        self.layout = QVBoxLayout(self)  # 创建一个布局并且把按钮添加上去
        self.layout.addWidget(self.button)

    @Slot()  # @Slot是一个将函数标识为槽的装饰器，应该始终使用以避免意外行为
    def click(self):
        print("clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWidget()
    w.show()

    # 注意，因为QPushButton也是QWidget的子类，所以可以脱离上面定义的MyWidget而存在
    button = QPushButton("Click me again!")
    button.clicked.connect(MyWidget.click)
    button.show()

    sys.exit(app.exec())
