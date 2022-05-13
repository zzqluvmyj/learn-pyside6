from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QHBoxLayout, QMenu
import sys
from PySide6.QtGui import QAction

"""
QPushButton 小部件提供了一个命令按钮

按钮或命令按钮可能是任何图形用户界面中最常用的小部件。按下（单击）按钮以命令计算机执行某些操作或回答问题。典型的按钮是确定、应用、取消、关闭、是、否和帮助。

命令按钮是矩形的，通常显示一个描述其操作的文本标签。可以通过在文本中在首选字符前加上 & 符号来指定快捷键。

按钮显示一个文本标签，以及一个可选的小图标。这些可以使用构造函数设置，稍后使用setText () 和setIcon () 进行更改。如果按钮被禁用，文本和图标的外观将根据 GUI 样式进行操作，以使按钮看起来“禁用”。

当鼠标、空格键或键盘快捷键激活按钮时，它会发出clicked () 信号。连接到此信号以执行按钮的操作。按钮还提供不太常用的信号，例如pressed() 和 released()。

默认情况下，对话框中的命令按钮是自动默认按钮，即当它们接收到键盘输入焦点时，它们会自动成为默认按钮。默认按钮是当用户在对话框中按下 Enter 或 Return 键时激活的按钮。您可以使用setAutoDefault ()更改此设置。请注意，自动默认按钮保留了一些额外的空间，这是绘制默认按钮指示器所必需的。如果您不希望按钮周围有这个空间，请调用setAutoDefault (false)。

由于如此重要​​，按钮小部件在过去十年中已经发展到可以适应许多变化。Microsoft 样式指南现在显示了大约十种不同的 Windows 按钮状态，并且文本暗示当考虑到所有功能组合时还有几十种。

最重要的模式或状态是：

可用或不可用（灰显、禁用）。
标准按钮、切换按钮或菜单按钮。
开或关（仅用于切换按钮）。
默认或正常。对话框中的默认按钮通常可以使用 Enter 或 Return 键“单击”。
是否自动重复。
按下与否。

作为一般规则，当应用程序或对话框窗口在用户单击它时执行操作（例如应用、取消、关闭和帮助）以及小部件应该具有宽的矩形形状和文本标签时，使用按钮。
用于更改窗口状态而不是执行操作的小而典型的方形按钮（例如QFileDialog右上角的按钮）不是命令按钮，而是工具按钮。Qt为这些按钮提供了一个特殊的类（ QToolButton ）。

如果您需要切换行为（参见setCheckable ()）或在按下时自动重复激活信号的按钮（如滚动条中的箭头）（参见setAutoRepeat ()），那么命令按钮可能不是您想要的。如有疑问，请使用工具按钮。

注意：在 macOS 上，当按钮的宽度小于 50 或高度小于 30 时，按钮的角会从圆形变为方形。使用setMinimumSize () 函数来防止这种行为。

命令按钮的一种变体是菜单按钮。它们不仅提供一个命令，而且提供多个命令，因为当它们被单击时，它们会弹出一个选项菜单。使用方法setMenu () 将弹出菜单与按钮相关联。

其他类别的按钮是选项按钮（请参阅QRadioButton）和复选框（请参阅QCheckBox）。

在 Qt 中，QAbstractButton基类提供了大部分模式和其他 API，QPushButton 提供了 GUI 逻辑。有关 API 的更多信息，请参阅QAbstractButton。

更多详细内容见：按钮抽象基类_QAbstractButton
"""


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setLayout(QHBoxLayout())

        self.button1 = QPushButton("好", self)
        self.layout().addWidget(self.button1)

        # 绑定命令
        self.button1.clicked.connect(self.you_command)

        # 设置为默认按钮，可以在获取焦点时自动选中
        self.button1.setDefault(True)
        print(self.button1.isDefault())

        # 设置自动默认按钮
        # 在某些 GUI 样式中，默认按钮的绘制周围有一个额外的框架，最多 3 个像素或更多。
        # Qt 会自动在自动默认按钮周围留出这个空间，即自动默认按钮可能有稍大的尺寸提示。
        # 对于具有QDialog父级的按钮，此属性的默认值为 true；否则默认为假。
        self.button1.setAutoDefault(True)

        # 设置按钮边框是否凸起（是否有按钮背景）
        # 此属性的默认值为 false。如果设置了这个属性，大多数样式不会绘制按钮背景，除非按钮被按下。
        # setAutoFillBackground () 可用于确保使用QPalette::Button画笔填充背景。
        self.button1.setFlat(True)
        print(self.button1.isFlat())

        # 设置弹出菜单
        self.menu = QMenu(self)  # 此时菜单的标题无关紧要，不会显示
        self.menu.addAction(QAction("你好", self))
        self.menu.addAction(QAction("我好", self))
        self.button1.setMenu(self.menu)

        self.button2 = QPushButton("好不好", self)
        # showMenu可以弹出设置的菜单
        self.button2.clicked.connect(lambda: self.button1.showMenu())
        self.layout().addWidget(self.button2)

    # 当设置弹出菜单后，不会触发clicked信号
    @Slot()
    def you_command(self):
        print("好")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
