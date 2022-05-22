import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QLabel

from PySide6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scroll_area = QScrollArea(self)
        self.setCentralWidget(self.scroll_area)
        self.label = QLabel(self)
        self.label.resize(200, 600)
        self.label.setTextFormat(Qt.MarkdownText)
        with open("./assets/hello.md", "r", encoding="utf8") as f:
            self.label.setText(f.read())

        # 设置QScrollArea的包含的小部件
        self.scroll_area.setWidget(self.label)

        self.menu = self.menuBar().addMenu("菜单")

        # void QScrollArea:: ensureVisible ( int x , int y , int xmargin = 50, int ymargin = 50)
        # 滚动滚动区域的内容，以便点 ( x , y ) 在视口区域内可见，其边距由xmargin和ymargin以像素为单位指定。
        # 如果无法到达指定点，则将内容滚动到最近的有效位置。两个边距的默认值为 50 像素。
        self.menu.addAction("确保(0,0)可见", lambda: self.scroll_area.ensureVisible(0, 0))

        # void QScrollArea:: ensureWidgetVisible ( QWidget * childWidget , int xmargin = 50, int ymargin = 50)
        # 滚动滚动区域的内容，以便QScrollArea ::widget ()的childWidget 在视口内可见，其边距由xmargin和ymargin以像素为单位指定。
        # 如果无法到达指定点，则将内容滚动到最近的有效位置。两个边距的默认值为 50 像素。
        self.menu.addAction(
            "确保小部件可见", lambda: self.scroll_area.ensureWidgetVisible(self.label)
        )

        # 此属性保存滚动区域是否应调整视图小部件的大小
        # 如果此属性设置为 false（默认值），则滚动区域遵循其小部件的大小。不管这个属性如何，
        # 你都可以使用widget ()-> resize ()以编程方式调整小部件的大小，滚动区域会自动调整到新的大小。
        # 如果此属性设置为 true，则滚动区域将自动调整小部件的大小，以避免滚动条可以避免，或者利用额外的空间。
        self.scroll_area.setWidgetResizable(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
