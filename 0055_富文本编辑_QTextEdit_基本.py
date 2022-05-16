import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Slot, Qt, QMargins, QPoint


"""
QTextEdit 是一个高级的所见即所得查看器/编辑器，支持使用 HTML 样式标签或 Markdown 格式的富文本格式。它经过优化以处理大型文档并快速响应用户输入。

QTextEdit 适用于段落和字符。段落是一个格式化的字符串，它被自动换行以适应小部件的宽度。默认情况下，在阅读纯文本时，一个换行符表示一个段落。一个文档由零个或多个段落组成。段落中的单词按照段落的对齐方式对齐。段落由硬换行符分隔。段落中的每个字符都有自己的属性，例如字体和颜色。

QTextEdit 可以显示图像、列表和表格。如果文本太大而无法在文本编辑的视口中查看，则会出现滚动条。文本编辑可以加载纯文本和富文本文件。富文本可以使用 HTML 4 标记的子集来描述；有关详细信息，请参阅支持的 HTML 子集页面。

如果您只需要显示一小段富文本，请使用QLabel。

Qt 中的富文本支持旨在提供一种快速、可移植和高效的方式来为应用程序添加合理的在线帮助工具，并为富文本编辑器提供基础。如果您发现 HTML 支持不足以满足您的需求，您可以考虑使用 Qt WebKit，它提供了一个全功能的 Web 浏览器小部件。

QTextEdit 上鼠标光标的形状默认为Qt::IBeamCursor。它可以通过viewport () 的 cursor 属性来改变。

更多见 https://doc.qt.io/qt-6/qtextedit.html
"""


class Window(QTextEdit):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.setAcceptRichText(False)
        # 是否接受用户插入的富文本
        # 当此属性设置为 false 时，文本编辑将仅接受来自用户的纯文本输入。例如通过剪贴板或拖放。
        # 此属性的默认值为 true。
        # 当为false时，用户复制的富文本粘贴后会变成纯文本

        self.setAlignment(Qt.AlignLeft)
        # 设置对齐

        self.setAutoFormatting(QTextEdit.AutoAll)
        # 设置自动格式化
        # 目前仅支持自动项目符号列表。
        # 即自动创建项目符号列表（例如，当用户在最左侧的列中输入星号 ('*') 或在现有列表项中按 Enter 时。

        self.setCursorWidth(10)
        # 设置光标的宽度

        self.setReadOnly(False)
        # 设置是否只读

        self.setLineWrapMode(QTextEdit.FixedColumnWidth)
        # 设置换行模式
        # 枚举值如下
        # QTextEdit::NoWrap	0
        # QTextEdit::WidgetWidth	1
        # QTextEdit::FixedPixelWidth	2
        # QTextEdit::FixedColumnWidth    3
        # 默认模式是WidgetWidth，它会导致文字在文本编辑的右边缘被换行。换行发生在空白处，保持整个单词完整。
        # 如果您希望在单词中发生换行，请使用setWordWrapMode ()。
        # 如果您设置了FixedPixelWidth或FixedColumnWidth的换行模式，您还应该使用所需的宽度调用setLineWrapColumnOrWidth ()。

        self.setLineWrapColumnOrWidth(10)
        # 如果换行模式为FixedPixelWidth，则该值是从文本编辑的左边缘算起文本应该被换行的像素数。
        # 如果换行模式为FixedColumnWidth，则该值是从文本编辑的左边缘开始的列号（以字符列为单位），文本应在该处换行。
        # 默认情况下，此属性包含值 0。

        # void	setWordWrapMode(QTextOption::WrapMode policy)
        # 省略，因为用不到单词

        self.setOverwriteMode(False)
        # 新文本是否覆盖现有的文本，默认为False

        self.setPlaceholderText("hello QTextEdit")
        # 设置占位符

        self.setTabChangesFocus(False)
        # tab是否更改焦点或接受为输入，默认为false，即不会更改焦点且会接受tab作为输入

        self.setTabStopDistance(10)
        # 设置tab的所能代表的距离

        self.setTextInteractionFlags(Qt.TextEditorInteraction)
        # 指定小部件应如何与用户输入交互。一般用默认值不用设置
        # 默认值取决于QTextEdit是只读的还是可编辑的，以及它是否是QTextBrowser。
        # 具体见https://doc.qt.io/qt-6/qt.html#TextInteractionFlag-enum




if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec())
