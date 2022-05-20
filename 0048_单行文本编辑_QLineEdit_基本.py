import sys
from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Slot, Qt, QMargins


"""
QLineEdit 小部件是一个单行文本编辑器

单行编辑允许用户使用一组有用的编辑功能输入和编辑单行纯文本，包括撤消和重做、剪切和粘贴以及拖放（参见setDragEnabled ()）。

通过更改行编辑的echoMode ()，它也可以用作“只写”字段，用于密码等输入。

文本的长度可以限制为maxLength ()。可以使用validator()  或inputMask () 或两者来任意约束文本。在同一行编辑中在验证器和输入掩码之间切换时，最好清除验证器或输入掩码以防止未定义的行为。

一个相关的类是QTextEdit，它允许多行、富文本编辑。

您可以使用setText () 或insert ()更改文本。使用text () 检索文本；使用displayText ()检索显示的文本（可能不同，请参阅EchoMode）。可以用setSelection ()或selectAll ()选择文本，选择可以cut(), copy()ied and paste()。文本可以用setAlignment () 对齐。

当文本发生变化时，会发出textChanged () 信号；当文本发生变化而不是通过调用setText ()时，会发出textEdited () 信号；当光标移动时，会发出cursorPositionChanged () 信号；当按下 Return 或 Enter 键时，会发出returnPressed () 信号。

编辑完成后，无论是因为行编辑失去焦点还是按下 Return/Enter，都会发出editingFinished () 信号。请注意，如果在没有进行任何更改的情况下失去焦点，则不会发出editingFinished () 信号。

请注意，如果在行编辑上设置了验证器，则仅当验证器返回QValidator::Acceptable时才会发出returnPressed ()/ editingFinished () 信号。

默认情况下，QLineEdits 有一个由平台样式指南指定的框架；您可以通过调用setFrame (false)将其关闭。

默认键绑定如下所述。行编辑还提供了一个上下文菜单（通常通过鼠标右键单击来调用）

更多见https://doc.qt.io/qt-6/qlineedit.html
"""


class Window(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setWindowTitle("你好")
        self.setLayout(QFormLayout(self))

        self.layout().addRow("0-默认", QLineEdit())

        # action
        self.line_edit_1 = QLineEdit(self)
        # self.action1 = QAction("你好", self)
        # 上面的action不显示文字，暂不知为何，只能使用图标的action
        self.action1 = self.line_edit_1.addAction(
            QIcon("./assets/refresh.png"), QLineEdit.TrailingPosition
        )
        self.action1.triggered.connect(lambda: print("文本已刷新"))
        self.layout().addRow("1-action", self.line_edit_1)

        # 对齐
        self.line_edit_2 = QLineEdit(self)
        self.line_edit_2.setAlignment(Qt.AlignRight)
        # 其他布局见官方文档或垂直布局_基本
        self.layout().addRow("2-对齐", self.line_edit_2)

        # 光标移动风格
        self.line_edit_3 = QLineEdit(self)
        # self.line_edit_3.setCursorMoveStyle(Qt.VisualMoveStyle)
        # VisualMoveStyle表示无论是从左到右还是从右到左，左键光标一定向左移动，右键一定向右移动
        self.line_edit_3.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.layout().addRow("3-光标移动风格", self.line_edit_3)

        self.line_edit_4 = QLineEdit(self)
        self.line_edit_4.setDragEnabled(True)
        # 如果为True，某些选定文本上按下并移动鼠标，可以移动复制选中文本
        self.layout().addRow("4-可拖拽", self.line_edit_4)

        # 回显模式确定在行编辑中输入的文本如何显示（或回显）给用户。
        # 最常见的设置是Normal，其中用户输入的文本被逐字显示，但QLineEdit也支持允许输入文本被抑制或隐藏的模式
        # 这些模式包括NoEcho、Password和PasswordEchoOnEdit。
        # 小部件的显示以及复制或拖动文本的能力受此设置的影响。
        # 默认情况下，此属性设置为Normal。
        self.line_edit_5 = QLineEdit(self)
        self.line_edit_5.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.layout().addRow("5-回显模式", self.line_edit_5)

        # 如果启用（默认）则有边框，否则没有边框
        self.line_edit_6 = QLineEdit(self)
        self.line_edit_6.setFrame(False)
        self.layout().addRow("6-边框", self.line_edit_6)

        # 启用清理按钮
        self.line_edit_7 = QLineEdit(self)
        self.line_edit_7.setClearButtonEnabled(True)
        self.layout().addRow("7-清理按钮", self.line_edit_7)

        # 在只读模式下，用户仍然可以将文本复制到剪贴板，或者拖放文本（如果echoMode () 为Normal），但不能对其进行编辑。
        # QLineEdit在只读模式下不显示光标。
        # 默认情况下，此属性为false.
        # ERROR：只读有bug，中文依然能够输入
        self.line_edit_8 = QLineEdit(self)
        self.line_edit_8.setText("hello world")
        self.line_edit_8.setReadOnly(True)
        self.layout().addRow("8-只读", self.line_edit_8)

        # 如果文本太长，则在限制处截断。
        # 如果发生截断，任何选定的文本都将被取消选择，光标位置设置为 0 并显示字符串的第一部分。
        # 如果行编辑具有输入掩码，则掩码定义最大字符串长度。
        # 默认情况下，此属性包含值 32767。
        # 注意：utf8字符长度计算正确
        self.line_edit_9 = QLineEdit(self)
        self.line_edit_9.setMaxLength(5)
        self.layout().addRow("9-最大长度", self.line_edit_9)

        # 只要行编辑为空，设置此属性会使行编辑显示为灰色的占位符文本。
        # 通常，空行编辑会显示占位符文本，即使它具有焦点。
        # 但是，如果内容水平居中，则当行编辑具有焦点时，占位符文本不会显示在光标下。
        self.line_edit_10 = QLineEdit(self)
        self.line_edit_10.setAlignment(Qt.AlignCenter)
        self.line_edit_10.setPlaceholderText("姓名")
        self.layout().addRow("10-占位符", self.line_edit_10)

        # 设置框架和文本的间距
        self.line_edit_11 = QLineEdit(self)
        self.line_edit_11.setTextMargins(10, 10, 10, 10)
        self.line_edit_11.setTextMargins(QMargins(10, 10, 10, 10))
        self.layout().addRow("11-间距", self.line_edit_11)

        # 设置和读取文本
        self.line_edit_12 = QLineEdit(self)
        self.line_edit_12.setText("hello world")
        print(self.line_edit_12.text())
        self.layout().addRow("12-文本", self.line_edit_12)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec())
