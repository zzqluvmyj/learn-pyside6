import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QSize

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 虽然QWidget类的__init__函数不接受这些形参
    # 但是因为QWidget含有这些属性
    # 所以可以用kwargs的方式来传入参数
    # 虽然我也不知道怎么办到的，源码我是看不懂的
    # 这样可以避免调用各种属性的访问方法
    # 虽然没有代码提示，且不利于维护，但减少了代码量
    # 总体来说不推荐，宁可多写几行代码页不要这么写
    w = QWidget(windowTitle="简化属性设置", size=QSize(300, 300), toolTip="这是提示")

    w.setWindowTitle("hello world")  # 设置标题
    w.show()

    sys.exit(app.exec())
