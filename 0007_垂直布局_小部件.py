import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # self.layout = QVBoxLayout(self)
        # 或者
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # addWidget: (arg__1: QWidget, stretch: int = ..., alignment: Alignment = ...) -> None
        # 其中stretch是拉伸比例，该值越大，拉伸时变化越快
        # alignment是布局，有以下取值

        # 水平标志
        # Qt.AlignLeft  左对齐
        # Qt.AlignRight  右对齐
        # Qt.AlignHCenter  横向水平对齐
        # Qt.AlignJustify  对齐可用空间中的文本

        # 垂直标志
        # Qt.AlignTop  顶部对齐
        # Qt.AlignBottom  底部对齐
        # Qt.AlignVCenter  垂直水平对齐

        # 水平垂直标志
        # Qt.AlignCenter  水平且垂直居中（相当于AlignHCenter|AlignVCenter）
        # 最多可以使用一个水平标志和一个垂直标志
        # 多个标志一起使用的时候按位与 |

        # 其他
        # Qt.AlignAbsolute
        # 如果小部件的布局方向是从右到左,而不是默认的从左到右
        # 那么Qt.AlignLeft会指向右边缘
        # 如果仍然要使Qt.AlignLeft指向左边缘,按位与Qt.AlignAbsolute
        # Qt.AlignLeading  Qt.AlignLeft 的同义词
        # Qt.AlignTrailing  Qt.AlignRight 的同义词

        # 如果标志发生了冲突,则是未定义的含义(这个应该没用)
        # Qt.AlignHorizo​​ntal_Mask
        # Qt.AlignVertical_Mask

        self.layout.addWidget(QLabel("label 1"), 1, Qt.AlignLeft)
        self.layout.addWidget(QLabel("label 2"), 2, Qt.AlignLeft)
        self.layout.addWidget(QLabel("label 3"), 2, Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.resize(200, 200)
    w.show()
    # 设置QLabel的样式边框，便于查看
    app.setStyleSheet(
        """
        QLabel {
            border:1px solid;
        }
    """
    )
    app.exec()
