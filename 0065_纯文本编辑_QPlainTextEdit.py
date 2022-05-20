import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
)
from PySide6.QtCore import Slot, QRect
from PySide6.QtGui import QPalette


"""
QPlainTextEdit 是支持纯文本的高级查看器/编辑器。它经过优化以处理大型文档并快速响应用户输入。

QPlainText 使用与QTextEdit非常相同的技术和概念，但针对纯文本处理进行了优化。

QPlainTextEdit 适用于段落和字符。段落是一个格式化的字符串，它被自动换行以适应小部件的宽度。默认情况下，在阅读纯文本时，一个换行符表示一个段落。一个文档由零个或多个段落组成。段落由硬换行符分隔。段落中的每个字符都有自己的属性，例如字体和颜色。

QPlainTextEdit 上鼠标光标的形状默认为Qt::IBeamCursor。它可以通过viewport () 的 cursor 属性来改变。

QPlainTextEdit继承自QTextEdit，基本上和QTextEdit没什么不同，
以下仅仅展示和QTextEdit所不同的一些情况
"""


"""
信号
void	blockCountChanged(int newBlockCount)
每当块计数发生变化时，都会发出此信号。新的块计数在newBlockCount中传递。

void	modificationChanged(bool changed)
每当文档的内容以影响修改状态的方式发生变化时，就会发出此信号。如果changed为真，则文档已被修改；否则为假。
例如，在文档上调用 setModified(false) 然后插入文本会导致信号被发出。如果您撤消该操作，导致文档返回到其原始未修改状态，则信号将再次发出

void	updateRequest(const QRect &rect, int dy)
当文本文档需要更新指定的rect时，会发出此信号。如果文本滚动，rect将覆盖整个视口区域。如果文本垂直滚动，则dy携带视口滚动的像素数量。
该信号的目的是支持纯文本编辑子类中的额外小部件，例如显示行号、断点或其他额外信息。
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ptext_edit = QPlainTextEdit(self)
        self.setCentralWidget(self.ptext_edit)

        p = QPalette()
        p.setColor(QPalette.Base, "green")
        self.setPalette(p)
        self.ptext_edit.setViewportMargins(10, 10, 10, 10)
        # self.ptext_edit.setBackgroundVisible(True)
        # 调色板背景在文档区域之外是否可见
        # 如果设置为 true，纯文本编辑将在文本文档未覆盖的视口区域上绘制调色板背景。否则，如果设置为 false，则不会。该功能使用户可以在视觉上区分使用调色板的基色绘制的文档区域和未被任何文档覆盖的空白区域。
        # 默认值为假。
        # 仅仅对于调色板生效，对qss无效

        self.ptext_edit.setLineWrapMode(QPlainTextEdit.NoWrap)
        # setLineWrapMode(QPlainTextEdit mode)
        # 和QTextEdit不同，此处仅有两个枚举值
        # QPlainTextEdit::NoWrap	0
        # QPlainTextEdit::WidgetWidth	1  (默认)

        self.menu = self.menuBar().addMenu("菜单")

        self.menu.addAction("文本块数量", lambda: print(self.ptext_edit.blockCount()))
        # blockCount 保存文档中文本块的数量。默认情况下，在空文档中，此属性包含值 1。

        self.menu.addAction("光标垂直居中", lambda: self.ptext_edit.centerCursor())

        self.menu.addAction(
            "设置文档未被修改", lambda: self.ptext_edit.document().setModified(False)
        )

        self.ptext_edit.setCenterOnScroll(False)
        # 设置光标在屏幕上居中

        self.ptext_edit.setMaximumBlockCount(10)
        # 指定文档可能具有的最大块数。如果文档中有更多使用此属性指定的块，则从文档的开头删除块。
        # 负值或零值指定文档可能包含无限数量的块。
        # 默认值为 0。
        # 请注意，设置此属性将立即将限制应用于文档内容。设置此属性还会禁用撤消重做历史记录。
        # 适用于做日志显示

        self.ptext_edit.appendHtml("<h1>hello</h1>")
        # 使用appendHtml () 附加 html 格式的文本。
        # 虽然 QPlainTextEdit 不支持使用表格和浮点数进行复杂的富文本渲染，
        # 但它确实支持您在日志查看器中可能需要的有限的基于段落的格式。

        self.ptext_edit.appendPlainText("<h1>hello</h1>")
        # 添加纯文本

        self.ptext_edit.blockCountChanged.connect(self.block_count_changed)
        self.ptext_edit.modificationChanged.connect(self.modification_changed)
        self.ptext_edit.updateRequest.connect(self.update_request)

    @Slot(int)
    def block_count_changed(self, newBlockCount):
        print("block_count_changed", newBlockCount)

    @Slot(bool)
    def modification_changed(self, changed):
        print("modification_changed", changed)

    @Slot(QRect, int)
    def update_request(self, rect, dy):
        print("update_request", rect, dy)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
