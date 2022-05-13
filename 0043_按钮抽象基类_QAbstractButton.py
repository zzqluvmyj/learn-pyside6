"""
这个类实现了一个抽象按钮。此类的子类处理用户操作，并指定按钮的绘制方式。

QAbstractButton 支持按钮和可选中（Checkable）按钮。可选中按钮在QRadioButton和QCheckBox类中实现。
按钮在QPushButton和QToolButton类中实现；如果需要，这些还提供切换行为。

任何按钮都可以显示包含文本和图标的标签。setText () 设置文本；setIcon () 设置图标。如果一个按钮被禁用，它的标签会被改变，使按钮具有“禁用”的外观。

如果按钮是一个文本按钮，其字符串包含一个与号 ('&')，QAbstractButton 会自动创建一个快捷键。

具体请参阅QShortcut文档。要显示实际的 & 符号，请使用“&&”。

您还可以使用setShortcut () 函数设置自定义快捷键。这主要用于没有任何文本的按钮，因此不能有任何自动快捷方式。

Qt 提供的所有按钮（QPushButton、QToolButton、QCheckBox和QRadioButton）都可以显示文本和图标。

可以通过QPushButton::setDefault () 和QPushButton::setAutoDefault () 使按钮成为对话框中的默认按钮。

QAbstractButton 提供了用于按钮的大部分状态：
- isDown () 表示按钮是否被按下。
- isChecked () 表示按钮是否被选中。只有可选中的按钮（isCheckable()为True）可以被选中和取消选中（见下文）。
- isEnabled () 表示按钮是否可以被用户按下。
注意：与其他小部件相反，从 QAbstractButton 派生的按钮在禁用时接受鼠标和上下文菜单事件。
- setAutoRepeat () 设置按钮是否在用户按住时自动重复。autoRepeatDelay和autoRepeatInterval定义了如何完成自动重复。
- setCheckable () 设置按钮是否为切换按钮。

isDown ()和isChecked ()的区别如下。
当用户单击一个切换按钮进行选中时，该按钮首先被按下然后释放到选中状态。
当用户再次单击它（取消选中它）时，按钮首先移动到按下状态，然后进入未选中状态（isChecked（）和isDown（）都是false的）。

QAbstractButton 提供四个信号：
- pressed(): 当鼠标光标在按钮内时按下鼠标左键时会发出。
- released(): 当鼠标左键被释放时。
- clicked():
  - 在按钮第一次按下然后释放时发出
  - 在键入快捷键时
  - 在调用click()或animateClick()时发出。
- toggled(): 当切换按钮的状态发生变化时，会发出。

要继承 QAbstractButton，您必须至少重新实现paintEvent () 以绘制按钮的轮廓及其文本或像素图。
通常建议重新实现sizeHint ()，有时也重新实现hitButton ()（以确定按钮按下是否在按钮内）。
对于具有两个以上状态的按钮（如三态按钮），您还必须重新实现checkStateSet () 和nextCheckState ()。

具体见 https://doc.qt.io/qt-6/qabstractbutton.html
"""


"""
QAbstractButton提供的公共方法有

bool	autoExclusive() const
void	setAutoExclusive(bool)
如果启用了自动排他性，则属于同一父窗口小部件的可选中按钮的行为就像它们是同一排他按钮组（QButtonGroup）的一部分一样。
独占按钮组中，任何时候只能勾选一个按钮；选中另一个按钮会自动取消选中之前选中的按钮。
该属性对属于按钮组的按钮没有影响。
autoExclusive 默认关闭，单选按钮除外。

bool	autoRepeat() const
void	setAutoRepeat(bool)
如果启用了 autoRepeat，则按下按钮时会定期发出pressed(), released(), and clicked()  信号。自动重复默认关闭。初始延迟和重复间隔由autoRepeatDelay和autoRepeatInterval以毫秒为单位定义。
注意：如果一个按钮被一个快捷键按下，那么自动重复是由系统而不是这个类来启用和计时的。pressed(), released(), and clicked()  信号将像正常情况一样发出。

int	autoRepeatDelay() const
void	setAutoRepeatDelay(int)
见autoRepeat()

int	autoRepeatInterval() const
void	setAutoRepeatInterval(int)
见autoRepeat()

QButtonGroup *	group() const
返回此按钮所属的QButtonGroup。
如果按钮不是任何QButtonGroup的成员，则此函数返回nullptr。
见QButtonGroup

QIcon	icon() const
void	setIcon(const QIcon &icon)
设置或返回按钮图标

QSize	iconSize() const
此属性保存用于此按钮的图标大小。
默认大小由 GUI 样式定义。这是图标的最大尺寸。较小的图标不会被放大。

bool	isCheckable() const
void	setCheckable(bool)
此属性保存按钮是否可选中
默认情况下，该按钮是不可选中的。

bool	isChecked() const
是否选中，只能查看可选中的按钮

bool	isDown() const
void	setDown(bool)
如果此属性为true，则按下按钮。如果将此属性设置为 true，则不会发出 pressed() and clicked()的信号。默认值为假。

QKeySequence	shortcut() const
void	setShortcut(const QKeySequence &key)
此属性保存与按钮关联的助记符

QString	text() const
void	setText(const QString &text)
此属性保存按钮上显示的文本
如果按钮没有文本，text() 函数将返回一个空字符串。
如果文本包含 & 字符 ('&')，则会自动为其创建快捷方式。'&' 后面的字符将用作快捷键。
如果文本没有定义快捷方式，任何以前的快捷方式都将被覆盖或清除。
有关详细信息，请参阅QShortcut文档。要显示实际的 & 符号，请使用“&&”。
"""


"""
QAbstractButton提供的槽有

void	animateClick()
执行动画点击：立即按下按钮，并在 100 毫秒后释放。
在释放按钮之前再次调用此函数会重置释放计时器。
与点击相关的所有信号都会适当地发出。
如果按钮被禁用，此功能将不执行任何操作。

void	click()
执行单击。
与点击相关的所有常用信号都会酌情发出。如果该按钮是可选中的，则该按钮的状态被切换。
如果按钮被禁用，此功能将不执行任何操作。

void	setChecked(bool)
见isChecked()

void	setIconSize(const QSize &size)
见iconSize()

void	toggle()
切换可选中按钮的状态
"""


"""
QAbstractButton提供的信号有

void	clicked(bool checked = false)
当按钮被激活（即，当鼠标光标在按钮内时按下然后释放），当快捷键被键入，或者当click () 或animateClick () 被调用时，这个信号被发出。
值得注意的是，如果您调用setDown ()、setChecked () 或toggle ()，则不会发出此信号。
如果按钮是可选中的，如果按钮被选中，checked为真，如果按钮未被选中，则为假。

void	pressed()
该信号在按钮被按下时发出。

void	released()
释放按钮时发出此信号。

void	toggled(bool checked)
每当可检查按钮更改其状态时，都会发出此信号。如果按钮被选中， checked为真，如果按钮未被选中，则为假。
这可能是用户操作、click () 插槽激活或调用setChecked () 的结果。
独占按钮组中的按钮状态在此信号发出之前更新。
"""


from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QCheckBox,
    QRadioButton,
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setLayout(QVBoxLayout())

        # autoExclusive()
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(QCheckBox("1", self))
        self.layout1.addWidget(QCheckBox("2", self))
        self.layout1.addWidget(QCheckBox("3", self))
        self.layout().addLayout(self.layout1)

        # isCheckable()
        self.layout2 = QHBoxLayout()
        self.lb1 = QPushButton("是", self, checkable=True)
        self.lb2 = QPushButton("否", self, checkable=True)
        self.layout2.addWidget(self.lb1)
        self.layout2.addWidget(self.lb2)
        self.layout().addLayout(self.layout2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
