import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QCompleter,
    QWidget,
    QFileSystemModel,
)
from PySide6.QtCore import Qt, QStringListModel, Slot

"""
QCompleter 类提供基于项目模型的完成
您可以使用 QCompleter 在任何 Qt 小部件中提供自动完成功能，例如QLineEdit和QComboBox。
当用户开始输入单词时，QCompleter 会根据单词列表建议可能的完成单词的方法。
单词列表作为QAbstractItemModel提供。
（对于简单的应用程序，单词列表是静态的，您可以将QStringList传递给 QCompleter 的构造函数。）

QFileSystemModel可用于提供文件名的自动完成，但是尝试使用的时候没有生效，不知道为啥
TODO QTreeView和QFileSystemModel结合使用试试
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = QWidget(self)
        self.setCentralWidget(self.w)
        self.line_edit = QLineEdit(self.w)
        # 多套一个外部的widget是为了更好观察自动完成的视图情况
        self.c = QCompleter(self.w)
        self.line_edit.setCompleter(self.c)
        self.line_edit.returnPressed.connect(self.return_pressed)

        # 固定列表的作为自动完成源不再赘述
        # 下面使用QAbstractItemModel的形式
        # 其中QStringListModel是QAbstractItemModel的实现类

        # 创建QStringListModel并且指定数据
        self.m = QStringListModel(self.w)
        self.m.setStringList([str(i) for i in range(10000)] + ["aaa", "bbb", "ccc"])
        # 数量为10000时稍微有点卡，数量为100000太卡无法正常使用
        # 将创建的模型绑定到该自动完成对象
        self.c.setModel(self.m)

        # QStringListModel有很多方便的方法，更多见
        # https://doc.qt.io/qt-6/qstringlistmodel.html
        # 其实qt有这些方法是为了弥补c++的功能不足
        # 在python中其实可以整体生成新数据然后调用setStringList
        # 这两种方式哪个性能更好还不知道，如果有性能瓶颈或者优化性能的时候再来测试

        # 以上为QCompleter的基本使用流程
        # 以下为QCompleter的基本用法

        # 设置完成模式，取值如下
        # QCompleter::PopupCompletion	0	当前完成显示在弹出窗口中。
        # QCompleter::InlineCompletion	2	完成显示为内联（作为选定的文本）。
        # QCompleter::UnfilteredPopupCompletion	1	所有可能的完成都显示在弹出窗口中，最可能的建议指示为当前。
        self.c.setCompletionMode(QCompleter.PopupCompletion)

        # 此属性控制如何执行过滤。
        # 如果 filterMode 设置为Qt::MatchStartsWith，则只会显示那些以键入的字符开头的条目
        # Qt::MatchContains将显示包含输入字符的条目，Qt ::MatchEndsWith 将显示以输入字符结尾的条目。
        # 将 filterMode 设置为任何其他Qt::MatchFlag将发出警告，并且不会执行任何操作。
        # 因此，该Qt::MatchCaseSensitive标志无效。使用caseSensitivity属性来控制区分大小写。
        # 默认模式是Qt::MatchStartsWith。
        self.c.setFilterMode(Qt.MatchContains)

        # 设置允许屏幕上设置的最大尺寸
        self.c.setMaxVisibleItems(10)

        # 指定模型的排序方式
        # QCompleter::UnsortedModel	0	模型未排序。
        # QCompleter::CaseSensitivelySortedModel	1	该模型区分大小写。
        # QCompleter::CaseInsensitivelySortedModel	2	该模型不区分大小写。
        # 默认情况下，不对模型中提供完成的项目的顺序做出任何假设。
        # 如果completionColumn () 和completionRole () 的模型数据按升序排序，则可以将此属性设置为CaseSensitivelySortedModel或CaseInsensitivelySortedModel。在大型模型上，这可以显着提高性能，因为完成者对象可以使用二进制搜索算法而不是线性搜索算法。
        # 模型的排序顺序（即升序或降序）是通过检查模型的内容动态确定的。
        # 注意：当完成者的caseSensitivity与模型在排序时使用的区分大小写不同时，上述性能改进不会发生。
        self.c.setModelSorting(QCompleter.CaseInsensitivelySortedModel)

        # TODO setPopup可以指定弹出窗口，在QListView之后再进行补充

        # 设置大小写敏感性
        # Qt::CaseInsensitive	0
        # Qt::CaseSensitive	1
        self.c.setCaseSensitivity(Qt.CaseInsensitive)

        self.c.activated.connect(self.activated)
        self.c.highlighted.connect(self.highlighted)

    @Slot()
    def return_pressed(self):
        print("return_pressed")
        print("完成列", self.c.completionColumn())
        print("完成计数", self.c.completionCount())
        print("完成前缀", self.c.completionPrefix())
        print("当前完成", self.c.currentCompletion())
        print("当前索引", self.c.currentIndex())
        print("根据当前索引获取值", self.c.pathFromIndex(self.c.currentIndex()))
        print("当前行", self.c.currentRow())

    @Slot(str)
    def activated(self, s):
        print("activated", s)

    @Slot(str)
    def highlighted(self, s):
        print("highlighted", s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
