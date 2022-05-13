import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtGui import QKeySequence

"""
QKeySequence 类封装了快捷键使用的按键序列

在其最常见的形式中，键序列描述了必须一起使用才能执行某些操作的键组合。键序列与QAction对象一起使用，以指定可以使用哪些键盘快捷键来触发操作。

可以通过三种不同的方式构建键序列以用作键盘快捷键：
- 对于标准快捷键，可以使用标准键来请求与每个快捷键关联的特定于平台的键序列。
- 对于自定义快捷方式，可以使用诸如“Ctrl+X”之类的人类可读字符串，并且可以将这些字符串翻译成适合不同语言用户的快捷方式。翻译是在“ QShortcut ”上下文中进行的。
- 对于硬编码的快捷键，整数键码可以用Qt::Key和Qt::Modifier枚举值定义的值的组合来指定。每个键码由单个Qt::Key值和零个或多个修饰符组成，例如Qt::SHIFT、Qt::CTRL、Qt::ALT和Qt::META。
推荐使用标准快捷键，不推荐硬编码快捷键

更多见 https://doc.qt.io/qt-6/qkeysequence.html

QKeySequence有多个构造方法，如下所示，此处不再详述，用到来查就行
QKeySequence(QKeySequence::StandardKey key)
QKeySequence(const QKeySequence &keysequence)
QKeySequence(QKeyCombination k1, QKeyCombination k2 = QKeyCombination::fromCombined(0), QKeyCombination k3 = QKeyCombination::fromCombined(0), QKeyCombination k4 = QKeyCombination::fromCombined(0))
QKeySequence(int k1, int k2 = 0, int k3 = 0, int k4 = 0)
QKeySequence(const QString &key, QKeySequence::SequenceFormat format = NativeText)
"""


class Window(QPushButton):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setText("你好")
        # 设置按钮的快捷键
        # self.setShortcut("Ctrl+H")
        self.setShortcut(QKeySequence.Replace)  # 标准快捷键序列
        # self.setShortcut(QKeySequence("Ctrl+H"))
        self.clicked.connect(lambda: print("hello"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec())
