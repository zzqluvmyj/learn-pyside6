from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QLabel, QApplication
import sys


class Window(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(480, 720)

        self.setText(
            """<a href="链接地址1">链接名1</a> [链接名2](链接地址2) [hello](./assets/hello.md)"""
        )
        # 当设置为markdown格式后，md的链接也能触发linkHovered和linkActivated

        # 设置允许访问超链接
        # self.setOpenExternalLinks(True)

        # 设置链接的监听函数，以下是两个信号连接两个槽
        self.linkHovered.connect(self.link_hovered)
        self.linkActivated.connect(self.link_clicked)

        self.setTextFormat(Qt.MarkdownText)

    @Slot(str)
    def link_hovered(self, link):
        if link != "":
            print(link)

    @Slot(str)
    def link_clicked(self, link):
        if link != "":
            print(link)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
