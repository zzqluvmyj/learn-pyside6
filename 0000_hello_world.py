import sys
from PySide6.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()  # QWidget是所有可视化组件的基类
    w.resize(250, 200)
    w.move(300, 300)

    w.setWindowTitle("hello world")
    w.show()

    sys.exit(app.exec())
