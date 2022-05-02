import sys
from PySide6.QtWidgets import QMainWindow, QMenu, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

    # 重写contextMenuEvent
    def contextMenuEvent(self, event):

        file_menu = QMenu(self)

        new_file_action = file_menu.addAction("新建")
        open_file_action = file_menu.addAction("打开")
        quit_action = file_menu.addAction("退出")

        # 这是上下文菜单的关键
        file_menu.exec(event.globalPos())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.resize(200, 200)
    w.show()
    sys.exit(app.exec())
