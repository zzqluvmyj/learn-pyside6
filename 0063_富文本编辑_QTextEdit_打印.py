import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtPrintSupport import QPrinter

"""
void QTextEdit::print(QPagedPaintDevice *printer) const
将文本编辑的文档打印到给定打印机的便捷功能。这相当于直接在文档上调用 print 方法

TODO 更多更详细的打印例子
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.menu = self.menuBar().addMenu("菜单")
        self.menu.addAction("打印", self.print_pdf)

    def print_pdf(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("hello.pdf")
        self.text_edit.print_(printer)
        print("已打印到 hello.pdf")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
