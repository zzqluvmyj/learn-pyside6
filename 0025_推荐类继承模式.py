import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel


class Widget(QLabel):
    # 这样写__init__方法的原因如下：
    # 1.与库保持一致性
    # 2.如果parent=None，则为顶部窗口，否则为其他部件的子部件
    # 3.确保了父窗口在被垃圾回收的同时会回收子窗口
    # 类似内容参见0031
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText("你好")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    Widget(w)
    w.show()
    app.exec()
