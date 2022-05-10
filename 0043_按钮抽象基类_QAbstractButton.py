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

继承一个新的按钮类太过麻烦，下面使用QPushButton来演示之前没有涉及到的QAbstractButton提供的方法
"""
