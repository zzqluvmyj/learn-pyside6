import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread
import time

"""
使用Pyside6时，必须使用QThread，而不是python的线程，否则会出错


切记切记，线程的调度是系统自动执行的，是人不可控制的
千万不要以为线程可以随你的意愿想停就停想运行就运行
千万不要
线程的运行是不确定的，切记切记
"""


# 继承QThread并且重写run方法
class Worker(QThread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QMainWindow()  # QWidget是所有可视化组件的基类
    w.setWindowTitle("hello world")  # 设置标题
    w.show()

    t = Worker()
    t.start()

    sys.exit(app.exec())
