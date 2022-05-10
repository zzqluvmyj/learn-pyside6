import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication

# 继承QMainWindow才会有工具栏
# QToolBar控件是由文本按钮，图标或其他小控件按钮组成的可移动面板，通常位于菜单栏下方
# 更多见QToolButton
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        # 设置标题与初始大小
        self.setWindowTitle("toolbar例子")

        # 在工具栏区域添加文件工具栏
        tb = self.addToolBar("文件")  # 标题不会显示
        tb.addAction("新建")
        tb.addAction("打开")
        tb.addAction("保存")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
