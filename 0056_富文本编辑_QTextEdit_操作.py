# 编辑
# void	append(const QString &text)
# void	clear()
# void	copy()
# void	cut()
# void	insertHtml(const QString &text)
# void	insertPlainText(const QString &text)
# void	paste()
# void	redo()
# void	undo()
# void	scrollToAnchor(const QString &name)
# void	selectAll()

# 字体
# void	setCurrentFont(const QFont &f)
# void	setFontFamily(const QString &fontFamily)
# void	setFontItalic(bool italic)
# void	setFontPointSize(qreal s)
# void	setFontUnderline(bool underline)
# void	setFontWeight(int weight)

# 内容设置
# void	setHtml(const QString &text)
# void	setMarkdown(const QString &markdown)
# void	setPlainText(const QString &text)
# void	setText(const QString &text)

# 颜色
# void	setTextBackgroundColor(const QColor &c)
# void	setTextColor(const QColor &c)

# 缩放
# void	zoomIn(int range = 1)
# void	zoomOut(int range = 1)

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QTextDocument


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
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

        # TODO 完善以下
        self.edit_menu = self.menuBar().addMenu("编辑")
        self.font_menu = self.menuBar().addMenu("字体")
        self.color_menu = self.menuBar().addMenu("颜色")
        self.zoom_menu = self.menuBar().addMenu("缩放")
        self.content_menu = self.menuBar().addMenu("内容设置")

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
