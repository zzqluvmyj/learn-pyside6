import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# qt和python之间的事件通信是通过信号和插槽来实现的，信号相当于事件，插槽相当于处理该事件的方法
# 信号和插槽绑定后，触发了事件，插槽的方法才会执行


@Slot()  # @Slot是一个将函数标识为槽的装饰器，应该始终使用以避免意外行为
def click(self):
    print("clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    button = QPushButton("Click me again!")
    button.clicked.connect(click)
    button.show()

    sys.exit(app.exec())
