import sys
from PySide6.QtWidgets import QApplication, QLabel

# qss文件和css文件非常类似，但是需要指定 Widget 组件以及可选的对象名称
if __name__ == "__main__":
    app = QApplication()

    w1 = QLabel("This is a placeholder text")
    w1.show()
    w2 = QLabel("This is a placeholder text")
    w2.setObjectName("title")
    w2.show()

    with open("style1.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
