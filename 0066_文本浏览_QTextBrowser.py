import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextBrowser,
)

from PySide6.QtCore import Slot, QUrl
from PySide6.QtGui import QTextDocument

"""
此类扩展了QTextEdit（只读模式），添加了一些导航功能，以便用户可以跟踪超文本文档中的链接。

如果您想为您的用户提供可编辑的富文本编辑器，请使用QTextEdit。如果您想要一个没有超文本导航的文本浏览器，请使用QTextEdit，并使用QTextEdit::setReadOnly () 禁用编辑。如果您只需要显示一小段富文本，请使用QLabel。

文件来源和内容
QTextEdit的内容是用setHtml () 或setPlainText () 设置的，但 QTextBrowser 也实现了setSource () 函数，使得使用命名文档作为源文本成为可能。在搜索路径列表和当前文档工厂的目录中查找该名称。

如果文档名称以锚点结尾（例如 " #anchor"），文本浏览器会自动滚动到该位置（使用scrollToAnchor ()）。当用户单击超链接时，浏览器将调用setSource () 本身并使用链接的href值作为参数。您可以通过连接到sourceChanged () 信号来跟踪当前源。
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_browser = QTextBrowser(self)
        self.setCentralWidget(self.text_browser)
        self.text_browser.setSource("./assets/hello.md", QTextDocument.UnknownResource)
        # 设置文件源

        self.nav_menu = self.menuBar().addMenu("导航")

        self.nav_menu.addAction("后退", lambda: self.text_browser.backward())
        self.nav_menu.addAction("前进", lambda: self.text_browser.forward())
        self.nav_menu.addAction("首页", lambda: self.text_browser.home())
        self.nav_menu.addAction("重载", lambda: self.text_browser.reload())
        self.nav_menu.addAction(
            "设置源为world.md", lambda: self.text_browser.setSource("assets/world.md")
        )

        self.other_menu = self.menuBar().addMenu("其他")
        self.other_menu.addAction(
            "后退历史计数", lambda: print(self.text_browser.backwardHistoryCount())
        )
        self.other_menu.addAction(
            "前进历史计数", lambda: print(self.text_browser.forwardHistoryCount())
        )
        self.other_menu.addAction("清空历史记录", lambda: self.text_browser.clearHistory())
        self.other_menu.addAction(
            "历史后退1标题", lambda: print(self.text_browser.historyTitle(-1))
        )
        self.other_menu.addAction(
            "历史后退1url", lambda: print(self.text_browser.historyUrl(-1))
        )
        self.other_menu.addAction(
            "当前标题", lambda: print(self.text_browser.historyTitle(0))
        )
        self.other_menu.addAction(
            "当前url", lambda: print(self.text_browser.historyUrl(0))
        )
        self.other_menu.addAction(
            "是否可以后退", lambda: print(self.text_browser.isBackwardAvailable())
        )
        self.other_menu.addAction(
            "是否可以前进", lambda: print(self.text_browser.isForwardAvailable())
        )

        print(self.text_browser.searchPaths())
        # self.text_browser.setSearchPaths()
        # 存文本浏览器用于查找支持内容的搜索路径
        # QTextBrowser使用这个列表来定位图像和文档。
        # 默认情况下，此属性包含一个空列表(保存字符串类型)。

        self.text_browser.setOpenExternalLinks(True)
        # 指定QTextBrowser是否应该使用QDesktopServices::openUrl ()自动打开指向外部源的链接，而不是发出anchorClicked信号。
        # 如果它们的方案既不是文件也不是 qrc，则链接被视为外部链接
        # 默认为False

        self.text_browser.setOpenLinks(True)
        # 是否应自动打开用户尝试通过鼠标或键盘激活的链接。
        # 无论此属性的值如何，始终会发出anchorClicked信号。
        # 默认值是True。

        self.text_browser.anchorClicked.connect(self.anchorClicked)
        self.text_browser.backwardAvailable.connect(self.backwardAvailable)
        self.text_browser.forwardAvailable.connect(self.forwardAvailable)
        self.text_browser.highlighted.connect(self.highlighted)
        self.text_browser.historyChanged.connect(self.historyChanged)
        self.text_browser.sourceChanged.connect(self.sourceChanged)

    @Slot(QUrl)
    def anchorClicked(self, url: QUrl):
        print("anchorClicked", url)

    @Slot(bool)
    def backwardAvailable(self, available):
        print("backwardAvailable", available)

    @Slot(bool)
    def forwardAvailable(self, available):
        print("forwardAvailable", available)

    @Slot(QUrl)
    def highlighted(self, url):
        print("highlighted", url)

    @Slot()
    def historyChanged(self):
        print("historyChanged")

    @Slot(QUrl)
    def sourceChanged(self, src):
        print("sourceChanged", src)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
