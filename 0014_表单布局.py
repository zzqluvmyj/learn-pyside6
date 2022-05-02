import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # QFormLayout是为了方便表单而设计的，和其他布局没有本质区别
        self.layout = QFormLayout(self)
        # addRow(label: QWidget, field: QLayout) -> None
        # addRow(label: QWidget, field: QWidget) -> None
        # addRow(labelText: str, field: QLayout) -> None
        # addRow(labelText: str, field: QWidget) -> None
        # addRow(layout: QLayout) -> None
        # addRow(widget: QWidget) -> None

        self.layout.addRow(QLabel("名字"), QVBoxLayout())
        self.layout.addRow(QLabel("名字"), QLineEdit())
        self.layout.addRow("名字", QVBoxLayout())
        self.layout.addRow("名字", QLineEdit())
        self.layout.addRow(QVBoxLayout())
        self.layout.addRow(QLineEdit())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.resize(200, 200)
    w.show()
    app.exec()
