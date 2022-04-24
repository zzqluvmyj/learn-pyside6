import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("<h1>Hello World!</h1>")  # 文本支持html标签和样式
label.show()


app.exec()
