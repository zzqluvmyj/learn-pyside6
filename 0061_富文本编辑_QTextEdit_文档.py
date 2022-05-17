import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtCore import QUrl
from PySide6.QtGui import QTextDocument

"""
QTextDocument *	document() const
void	setDocument(QTextDocument *document)
document属性保存文本编辑器的基础文档。

QString	documentTitle() const
void	setDocumentTitle(const QString &title)
保存从文本解析的文档的标题。
默认情况下，对于新创建的空文档，此属性包含一个空字符串。


QVariant QTextEdit::loadResource ( int type , const QUrl & name )
加载由给定类型和名称指定的资源。
该函数是QTextDocument::loadResource () 的扩展。
TODO 该函数不知如何使用

TODO 更多见 QTextDocument
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        print(self.text_edit.document(), self.text_edit.documentTitle())
        d = QTextDocument(self)
        d.setHtml("<h1>hello</h1>")
        self.text_edit.setDocument(d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
