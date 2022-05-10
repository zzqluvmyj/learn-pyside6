import sys
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QToolButton

"""
工具按钮是一种特殊按钮，可提供对特定命令或选项的快速访问。与普通命令按钮不同，工具按钮通常不显示文本标签，而是显示图标。

工具按钮通常在使用 QToolBar::addAction () 创建新的QAction实例或使用QToolBar::addAction () 将现有操作添加到工具栏时创建。也可以以与任何其他小部件相同的方式构建工具按钮，并将它们与布局中的其他小部件一起排列。

工具按钮的一个经典用途是选择工具。例如，绘图程序中的“钢笔”工具。这将通过使用 QToolButton 作为切换按钮来实现（参见setCheckable ()）。

QToolButton 支持自动升起。在自动升起模式下，仅当鼠标指向按钮时，按钮才会绘制 3D 帧。当在QToolBar中使用按钮时，该功能会自动打开。用setAutoRaise ()改变它。

工具按钮的图标设置为QIcon。这使得为​​禁用和活动状态指定不同的像素图成为可能。当按钮的功能不可用时，使用禁用的像素图。当鼠标指针悬停在按钮上时，将显示活动像素图。

按钮的外观和尺寸可通过setToolButtonStyle () 和setIconSize () 进行调整。当在QMainWindow的QToolBar中使用时，按钮会自动调整为QMainWindow的设置（参见QMainWindow::setToolButtonStyle () 和QMainWindow::setIconSize ()）。除了图标，工具按钮还可以显示箭头符号，由arrowType指定。

工具按钮可以在弹出菜单中提供额外的选择。可以使用setMenu () 设置弹出菜单。使用setPopupMode () 来配置带有菜单集的工具按钮可用的不同模式。默认模式是 DelayedPopupMode，有时与 Web 浏览器中的“返回”按钮一起使用。按住按钮一会儿后，会弹出一个菜单，显示可能跳转到的页面列表。超时取决于样式，请参阅QStyle::SH_ToolButton_PopupDelay。
"""

# TODO: 未完待续


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        # 在工具栏区域添加文件工具栏
        tb = self.addToolBar("文件")
        self.qb = QToolButton(self)
        self.qb.setText("菜单")
        self.qb.setIcon(QIcon("./assets/setting.png"))
        tb.addWidget(self.qb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
