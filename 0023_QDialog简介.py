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

        # exec()和open()
        # exec()将对话框显示为模态对话框，在用户关闭之前一直阻塞。该函数返回一个DialogCode结果
        # open()将立即返回，不阻塞

        # accept()，reject()和done(n):
        # accept() 隐藏模式对话框并将结果代码设置为Accepted(1).
        # reject() 当对话框被用户拒绝或使用QDialog::Rejected(0)参数调用reject() 或done()时，将发出此信号。
        # 请注意，使用hide () 或setVisible (false)隐藏对话框时不会发出此信号。这包括在对话框可见时将其删除。
        # done(n) 关闭对话框并将其结果代码设置为 n。finished(n) 信号将发出n；如果n是QDialog::Accepted(1)或QDialog::Rejected(0)，
        # 则也将分别发出accepted() 或 rejected() 信号。
        # 如果此对话框使用 exec () 来显示，则 done() 也会导致本地事件循环完成，并且exec() 返回 n。
        # 与QWidget::close () 一样，如果设置了Qt::WA_DeleteOnClose标志，done() 将删除对话框。
        # 如果对话框是应用程序的主要小部件，则应用程序终止。如果对话框是最后一个关闭的窗口，则发出QGuiApplication::lastWindowClosed () 信号。

        # 更详细内容参见  https://doc.qt.io/qt-6/qdialog.html

        # 可以设置默认按钮，默认按钮在获取焦点时可以自动选中，用enter触发，见setDefault(bool)，注意：并不是按下enter后就会调用accept()
        # 如果用户在QDialog中按下 Esc 键，QDialog::r​​eject() 将被调用。这将导致窗口关闭：关闭事件不能被忽略。

        # 经过下面的connect后：
        # 如果accept，则exec()返回1
        # 如果reject，则exec()返回0
        # 如果done(n)，则exec()返回n

        layout = QHBoxLayout(dialog)
        button2 = QPushButton("取消", dialog)
        button2.clicked.connect(dialog.reject)
        button1 = QPushButton("确认", dialog)
        button1.clicked.connect(dialog.accept)
        button1.setDefault(True)  # 设置为默认按钮后，获取焦点时会自动选中
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
        # dialog.open()
        print(dialog.result())  # 这个也可以获取DialogCode结果


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DialogDemo()
    w.resize(200, 200)
    w.show()
    app.exec()
