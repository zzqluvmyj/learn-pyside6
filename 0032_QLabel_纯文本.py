from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QApplication
import sys

"""
QLabel用于显示文本或图像。不提供用户交互功能。
标签的视觉外观可以通过多种方式进行配置，并且可以用于为另一个小部件指定焦点助记键。

QLabel包含以下项目类型：纯文本，富文本，QPixmap，QMovie，数字
QMovie和setBuddy()方法不涉及，感觉比较鸡肋
"""


class Window(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(100, 100)

        # 调用setText(str)时，qt会猜测文本类型，除非明确定义了textformat
        self.setText("**你好呀我的宝贝我的宝贝**")
        print(self.text())  # 获取label的值

        # 设置对齐，对齐的常量值见0007
        # self.setAlignment(Qt.AlignRight)

        # 设置缩进，单位是像素
        self.setIndent(10)

        # 设置边距
        self.setMargin(10)

        # 是否换行
        self.setWordWrap(True)

        # 文本选中
        # self.setSelection(2, 5)  # 设置选中的文本，该方法仅仅在show()以后生效
        # self.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard)
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)  # 鼠标可选中文字
        print(self.hasSelectedText())  # 是否有文本选中
        print(self.selectedText())  # 选中的文本是什么

        # 设置文本格式，共有以下几种格式
        # Qt::PlainText	文本字符串被解释为纯文本字符串。
        # Qt::RichText	文本字符串被解释为富文本字符串。有关富文本的定义，请参阅支持的 HTML 子集。
        # Qt::AutoText	如果Qt::mightBeRichText () 返回，则文本字符串被解释为 Qt::RichText true，否则被解释为 Qt::PlainText。
        # Qt::MarkdownText	文本字符串被解释为 Markdown 格式的文本。这个枚举值是在 Qt 5.14 中添加的。
        self.setTextFormat(Qt.MarkdownText)  # 此处设置为markdown文本，支持markdown标记


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    w.setSelection(2, 5)
    app.exec()
