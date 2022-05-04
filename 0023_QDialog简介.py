from distutils.command.build import build
import sys
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
)
from PySide6.QtCore import Qt

# QDialog 是对话框窗口的基类。对话框主要用来执行短期任务，或与用户进行互动，它可以是模式的也可以是非模式的。
# 模式对话框阻塞其他窗口，直到做出某些操作
# 非模式对话框允许和其他窗口同时进行操作
class DialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("弹出对话框", self)
        self.button.clicked.connect(self.show_dialog)

    def show_dialog(self):

        dialog = QDialog()  # 创建QDialog

        # QDialog 有3个方法可以返回值，accept，reject，done(int)
        # 如果accept，则exec()返回1
        # 如果reject，则exec()返回0
        # 如果done(n)，则exec()返回n

        layout = QHBoxLayout(dialog)
        button1 = QPushButton("确认", dialog)
        button1.clicked.connect(dialog.accept)
        button2 = QPushButton("取消", dialog)
        button2.clicked.connect(dialog.reject)
        button3 = QPushButton("？", dialog)
        button3.clicked.connect(lambda: dialog.done(-1))
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        dialog.setLayout(layout)

        dialog.setWindowTitle("是否确认")

        # 设置窗口模式
        # Qt.NonModal：非模态，可以和程序的其他窗口进行交互
        # Qt.WindowModal:窗口模态，程序在未处理玩当前对话框时，将阻止和对话框的父窗口进行交互
        # Qt.ApplicationModal：应用程序模态，阻止和任何其他窗口进行交互

        dialog.setWindowModality(Qt.ApplicationModal)
        print(dialog.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DialogDemo()
    w.resize(200, 200)
    w.show()
    app.exec()
