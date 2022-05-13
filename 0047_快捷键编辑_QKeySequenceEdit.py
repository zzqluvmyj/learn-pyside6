import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QKeySequenceEdit,
    QVBoxLayout,
)
from PySide6.QtGui import QKeySequence
from PySide6.QtCore import Slot

"""
QKeySequenceEdit 小部件允许输入QKeySequence

这个小部件允许用户选择一个QKeySequence，它通常用作快捷方式。
录制在小部件接收焦点时启动，并在用户释放最后一个键后一秒钟结束。

方法
QKeySequence	keySequence() const

Slots
void	clear()
void	setKeySequence(const QKeySequence &keySequence)

Signals
void	editingFinished()
void	keySequenceChanged(const QKeySequence &keySequence)
"""


class Window(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setWindowTitle("你好")
        self.setLayout(QVBoxLayout())

        self.key_sequence_edit = QKeySequenceEdit(self)
        self.layout().addWidget(self.key_sequence_edit)
        self.label = QLabel(self)
        self.layout().addWidget(self.label)

        self.key_sequence_edit.editingFinished.connect(self.editing_finished)
        self.key_sequence_edit.keySequenceChanged.connect(self.key_sequence_changed)

    @Slot()
    def editing_finished(self):
        s = "editing_finished " + self.key_sequence_edit.keySequence().toString()
        self.label.setText(s)

    @Slot(QKeySequence)
    def key_sequence_changed(self, key):
        """
        注意：
        每次快捷键编辑器改变时，都会先为空然后再为新的字符序列
        所以每次改变会引发两次keySequenceChanged事件
        而第二次事件和editingFinished有重合，应该是editingFinished信号在后
        所以在label中不会显示key_sequence_changed后加key
        """
        s = "key_sequence_changed " + key.toString()
        self.label.setText(s)
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec())
