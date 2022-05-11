import sys
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QToolButton, QMenu
from PySide6.QtCore import Qt

"""
工具按钮是一种特殊按钮，可提供对特定命令或选项的快速访问。与普通命令按钮不同，工具按钮通常不显示文本标签，而是显示图标。

工具按钮通常在使用 QToolBar::addAction () 创建新的QAction实例或使用QToolBar::addAction () 将现有操作添加到工具栏时创建。也可以以与任何其他小部件相同的方式构建工具按钮，并将它们与布局中的其他小部件一起排列。

工具按钮的一个经典用途是选择工具。例如，绘图程序中的“钢笔”工具。这将通过使用 QToolButton 作为切换按钮来实现（参见setCheckable ()）。

QToolButton 支持自动升起。在自动升起模式下，仅当鼠标指向按钮时，按钮才会绘制 3D 帧。当在QToolBar中使用按钮时，该功能会自动打开。用setAutoRaise ()改变它。

工具按钮的图标设置为QIcon。这使得为​​禁用和活动状态指定不同的像素图成为可能。当按钮的功能不可用时，使用禁用的像素图。当鼠标指针悬停在按钮上时，将显示活动像素图。

按钮的外观和尺寸可通过setToolButtonStyle () 和setIconSize () 进行调整。当在QMainWindow的QToolBar中使用时，按钮会自动调整为QMainWindow的设置（参见QMainWindow::setToolButtonStyle () 和QMainWindow::setIconSize ()）。除了图标，工具按钮还可以显示箭头符号，由arrowType指定。

工具按钮可以在弹出菜单中提供额外的选择。可以使用setMenu () 设置弹出菜单。使用setPopupMode () 来配置带有菜单集的工具按钮可用的不同模式。默认模式是 DelayedPopupMode，有时与 Web 浏览器中的“返回”按钮一起使用。按住按钮一会儿后，会弹出一个菜单，显示可能跳转到的页面列表。超时取决于样式，请参阅QStyle::SH_ToolButton_PopupDelay。
"""


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        # 在工具栏区域添加文件工具栏
        tb = self.addToolBar("文件")

        # 新建工具按钮并添加
        self.tool_button1 = QToolButton(self)
        self.tool_button2 = QToolButton(self)
        self.tool_button3 = QToolButton(self)
        tb.addWidget(self.tool_button1)
        tb.addWidget(self.tool_button2)
        tb.addWidget(self.tool_button3)

        # 设置按钮文字
        self.tool_button1.setText("设置")  # 默认情况下显示图标后不显示文本，用setToolButtonStyle来控制
        self.tool_button2.setText("更多")
        self.tool_button3.setText("其他")

        # 设置图标
        self.tool_button1.setIcon(QIcon("./assets/setting.png"))

        # 设置工具按钮样式
        # 枚举值有
        # Qt::ToolButtonIconOnly		只显示图标。
        # Qt::ToolButtonTextOnly		只显示文本。
        # Qt::ToolButtonTextBesideIcon		文本出现在图标旁边。
        # Qt::ToolButtonTextUnderIcon		文本出现在图标下方。
        # Qt::ToolButtonFollowStyle		遵循风格。
        self.tool_button1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 设置箭头图标
        # 枚举值有
        # Qt::NoArrow
        # Qt::UpArrow
        # Qt::DownArrow
        # Qt::LeftArrow
        # Qt::RightArrow
        self.tool_button2.setArrowType(Qt.DownArrow)

        # 设置自动提升，即扁平化效果
        self.tool_button2.setAutoRaise(False)

        # 设置弹出菜单模式
        # 枚举值有
        # QToolButton::DelayedPopup		按住工具按钮一段时间后（超时取决于样式，请参阅QStyle::SH_ToolButton_PopupDelay），将显示菜单。一个典型的应用示例是某些 Web 浏览器工具栏中的“后退”按钮。如果用户单击它，浏览器会简单地浏览回上一页。如果用户按住按钮一段时间，工具按钮会显示一个包含当前历史列表的菜单
        # QToolButton::MenuButtonPopup		在这种模式下，工具按钮会显示一个特殊的箭头，表示存在菜单。按下按钮的箭头部分时显示菜单。
        # QToolButton::InstantPopup		当按下工具按钮时，菜单会立即显示。在这种模式下，按钮自身的动作不会被触发。
        self.tool_button3.setPopupMode(QToolButton.MenuButtonPopup)

        # 设置默认的action
        # 注意：设置默认action时，会替代原来按钮的text
        self.action = QAction("我替代了其他", self)
        self.action.triggered.connect(lambda: print("hello"))
        self.tool_button3.setDefaultAction(self.action)

        # 设置弹出菜单并且监听该工具按钮上所有的action
        # ERROR
        # 注意：
        # 设置弹出菜单后，不知为什么，点击按钮无法弹出菜单
        # 但是showMenu()是可以用的
        # 所以下面把工具按钮3的信号绑定到了trigger上
        self.menu = QMenu(self.tool_button1)
        self.menu.addAction(QAction("11", self))
        self.menu.addAction(QAction("11", self))
        self.tool_button1.setMenu(self.menu)
        print(self.tool_button1.menu())

        self.tool_button3.triggered.connect(self.trigger)

    def trigger(self, action):
        self.tool_button1.showMenu()
        print(action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
