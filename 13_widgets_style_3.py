import sys
import random
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QWidget,
    QHBoxLayout,
    QApplication,
)
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])

    widget = Widget()
    widget.resize(800, 600)
    widget.show()

    with open("style2.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
