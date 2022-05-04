import sys
from PySide6.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()  # QWidget是所有可视化组件的基类
    w.setWindowTitle("hello world")  # 设置标题
    w.show()

    sys.exit(app.exec())
