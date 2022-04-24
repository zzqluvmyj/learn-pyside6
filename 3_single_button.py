# Signals and slots是 Qt 的一项功能，
# 它可以让您的图形小部件与其他图形小部件或您的 python 代码进行通信。


import sys  #
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


# @Slot ()是一个将函数标识为槽的装饰器。现在了解原因并不重要，但始终使用它来避免意外行为。
@Slot()
def say_hello():
    print("Button clicked, Hello!")


# Create the Qt Application
app = QApplication(sys.argv)
# Create a button
button = QPushButton("Click me")
# Connect the button to the function
button.clicked.connect(say_hello)
# Show the button
button.show()
# Run the main Qt loop
app.exec()
