import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtGui import QTextDocument


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.text_edit.setMarkdown("""<a href="https://cn.bing.com/">bing</a>""")

        self.menu = self.menuBar().addMenu("菜单")
        self.menu.addAction("输出html", self.print_html)
        self.menu.addAction("输出md-无html标签", self.print_md_nohtml)
        self.menu.addAction("输出md-CommonMark标准", self.print_md_common)
        self.menu.addAction("输出md-github方言(默认)", self.print_md_github)
        self.menu.addAction("输出纯文本", self.print_plain)

    def print_html(self):
        print(self.text_edit.toHtml())

    def print_md_nohtml(self):
        print(self.text_edit.toMarkdown(QTextDocument.MarkdownNoHTML))

    def print_md_common(self):
        print(self.text_edit.toMarkdown(QTextDocument.MarkdownDialectCommonMark))

    def print_md_github(self):
        print(self.text_edit.toMarkdown(QTextDocument.MarkdownDialectGitHub))
        # 默认值，推荐使用

    def print_plain(self):
        print(self.text_edit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
