import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QTextDocument, QColor, QFont


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.other_menu = self.menuBar().addMenu("查找")
        self.other_menu.addAction(
            '查找"abc"-向前匹配，不区分大小写，部分匹配',
            lambda: self.statusBar().showMessage(str(self.text_edit.find("abc"))),
        )
        self.other_menu.addAction(
            '查找"abc"-向后匹配',
            lambda: self.statusBar().showMessage(
                str(self.text_edit.find("abc", QTextDocument.FindBackward))
            ),
        )
        self.other_menu.addAction(
            '查找"abc"-区分大小写',
            lambda: self.statusBar().showMessage(
                str(self.text_edit.find("abc", QTextDocument.FindCaseSensitively))
            ),
        )
        self.other_menu.addAction(
            '查找"abc"-匹配完整单词',
            lambda: self.statusBar().showMessage(
                str(self.text_edit.find("abc", QTextDocument.FindWholeWords))
            ),
        )
        self.other_menu.addAction(
            '查找"abc"-正则表达式匹配数字',
            lambda: self.statusBar().showMessage(
                str(self.text_edit.find(QRegularExpression(r"\d")))
            ),
        )
        # TODO 更多见 QRegularExpression

        self.edit_menu = self.menuBar().addMenu("编辑")
        self.edit_menu.addAction(
            "增加html的h1", lambda: self.text_edit.append("<h1>hello</h1>")
        )
        self.edit_menu.addAction("增加md的#（无效）", lambda: self.text_edit.append("# hello"))
        self.edit_menu.addAction("清空", lambda: self.text_edit.clear())
        self.edit_menu.addAction("复制", lambda: self.text_edit.copy())
        self.edit_menu.addAction("剪切", lambda: self.text_edit.cut())
        self.edit_menu.addAction("粘贴", lambda: self.text_edit.paste())
        self.edit_menu.addAction(
            "插入html",
            lambda: self.text_edit.insertHtml(
                '<span style="color:white;background-color:black;">hello</span>'
            ),
        )
        self.edit_menu.addAction(
            "插入纯文本",
            lambda: self.text_edit.insertPlainText(
                '<span style="color:white;background-color:black;">hello</span>'
            ),
        )
        self.edit_menu.addAction("撤销", lambda: self.text_edit.undo())
        self.edit_menu.addAction("重做", lambda: self.text_edit.redo())
        self.edit_menu.addAction("全选", lambda: self.text_edit.selectAll())
        self.edit_menu.addAction(
            "滚动直到给定的锚可见（我是一个锚）", lambda: self.text_edit.scrollToAnchor("我是一个锚")
        )

        self.font_menu = self.menuBar().addMenu("字体")
        self.font_menu.addAction(
            "设置当前字体为楷体", lambda: self.text_edit.setCurrentFont(QFont("楷体"))
        )
        self.font_menu.addAction(
            "设置当前字体为仿宋", lambda: self.text_edit.setFontFamily("仿宋")
        )
        self.font_menu.addAction(
            "设置当前字体为斜体", lambda: self.text_edit.setFontItalic(True)
        )
        self.font_menu.addAction(
            "设置当前字体大小", lambda: self.text_edit.setFontPointSize(20)
        )
        self.font_menu.addAction(
            "设置当前字体为下划线", lambda: self.text_edit.setFontUnderline(True)
        )
        self.font_menu.addAction("设置当前字体粗细", lambda: self.text_edit.setFontWeight(10))
        # TODO 更多见QFont

        self.color_menu = self.menuBar().addMenu("颜色")
        self.color_menu.addAction(
            "当前格式的文本背景颜色为黑色",
            lambda: self.text_edit.setTextBackgroundColor(QColor("black")),
        )
        self.color_menu.addAction(
            "当前格式的文本颜色为白色", lambda: self.text_edit.setTextColor(QColor("white"))
        )
        # TODO 更多见QColor

        self.zoom_menu = self.menuBar().addMenu("缩放")
        self.zoom_menu.addAction("放大文本", lambda: self.text_edit.zoomIn(2))
        self.zoom_menu.addAction("缩小文本", lambda: self.text_edit.zoomOut(2))

        self.content_menu = self.menuBar().addMenu("内容设置")
        self.content_menu.addAction(
            "设置html",
            lambda: self.text_edit.setHtml(
                """<h1>111</h1>
<h2>222</h2>
"""
            ),
        )
        self.content_menu.addAction(
            "设置markdowm",
            lambda: self.text_edit.setMarkdown(
                """# title
- 111
- 222
- 333        
"""
            ),
        )
        self.content_menu.addAction(
            "设置纯文本",
            lambda: self.text_edit.setPlainText(
                """<h1>111</h1>
<h2>222</h2>
"""
            ),
        )
        self.content_menu.addAction("设置文本", lambda: self.text_edit.setText("12345"))
        # setText设置文本编辑的text。文本可以是纯文本或 HTML，文本编辑会尝试猜测正确的格式。
        # 直接使用setHtml () 或setPlainText () 避免文本编辑的猜测。

        self.other_menu = self.menuBar().addMenu("其他")
        self.other_menu.addAction(
            "移动到光标位置", lambda: self.text_edit.ensureCursorVisible()
        )
        self.other_menu.addAction(
            "剪贴板是否可粘贴",
            lambda: self.statusBar().showMessage(str(self.text_edit.canPaste())),
        )
        self.other_menu.addAction(
            "撤销和重做是否可用",
            lambda: self.statusBar().showMessage(
                str(self.text_edit.isUndoRedoEnabled())
            ),
        )
        self.other_menu.addAction(
            "撤销和重做不可用",
            lambda: self.text_edit.setUndoRedoEnabled(False),
        )
        self.other_menu.addAction(
            "撤销和重做可用（默认）",
            lambda: self.text_edit.setUndoRedoEnabled(True),
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
