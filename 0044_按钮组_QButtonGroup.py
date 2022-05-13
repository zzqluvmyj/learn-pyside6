from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QPushButton,
    QCheckBox,
    QRadioButton,
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QButtonGroup,
    QAbstractButton,
)
import sys

"""
QButtonGroup 类提供了一个容器来组织按钮小部件组

QButtonGroup 提供了一个抽象容器，可以在其中放置按钮小部件。
它不提供此容器的可视化表示（有关容器小部件，请参见QGroupBox），而是管理组中每个按钮的状态。

独占按钮组会关闭所有可选中（切换）按钮，但已单击的按钮除外。
默认情况下，按钮组是独占的。
按钮组中的按钮通常是可选中的QPushButton、QCheckBox（通常用于非独占按钮组）或QRadioButton。
如果创建独占按钮组，则应确保组中的一个按钮最初被选中；否则，该组最初将处于未选中任何按钮的状态。

可以使用addButton () 将按钮添加到组中，并使用removeButton () 将其删除。
如果该组是独占的，则当前选中的按钮可通过checkedButton () 获得。
如果单击按钮，则发出buttonClicked () 信号,对于排他组中的可选中按钮，这意味着该按钮已被选中。
组中的按钮列表由buttons() 返回。

此外，QButtonGroup 可以在整数和按钮之间进行映射。
您可以使用setId ()将整数 id 分配给按钮，并使用id ()检索它。
当前选中按钮的 id 可通过checkedId () 获得，
并且有一个重载信号buttonClicked () 会发出按钮的 id。
id为 -1 由 QButtonGroup 保留，表示“没有这样的按钮”。
映射机制的目的是简化枚举值在用户界面中的表示。
"""


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setLayout(QVBoxLayout())

        # QRadioButton默认，作为对比
        self.layout1 = QHBoxLayout()
        self.radio1 = QRadioButton("A", self)
        self.radio2 = QRadioButton("B", self)
        self.radio3 = QRadioButton("C", self)
        self.layout1.addWidget(QLabel("互斥radio-默认-无QButtonGroup"))
        self.layout1.addWidget(self.radio1)
        self.layout1.addWidget(self.radio2)
        self.layout1.addWidget(self.radio3)
        self.layout().addLayout(self.layout1)

        # QCheckBox默认，作为对比
        self.layout2 = QHBoxLayout()
        self.check1 = QCheckBox("A", self)
        self.check2 = QCheckBox("B", self)
        self.check3 = QCheckBox("C", self)
        self.layout2.addWidget(QLabel("互斥checkbox-默认-无QButtonGroup"))
        self.layout2.addWidget(self.check1)
        self.layout2.addWidget(self.check2)
        self.layout2.addWidget(self.check3)
        self.layout().addLayout(self.layout2)

        self.layout3 = QHBoxLayout()
        self.bg1 = QButtonGroup(self)
        self.radio1_1 = QRadioButton("A", self)
        self.radio1_2 = QRadioButton("B", self)
        self.radio1_3 = QRadioButton("C", self)
        self.radio1_4 = QRadioButton("D", self)
        # 添加按钮到QButtonGroup
        # addButton: (arg__1: QAbstractButton, id: int = -1) -> None
        # 如果id为-1，会自动分配一个id
        # 自动分配的id保证为负数，从-2开始
        # 如果要自己分配id，请使用正数以避免冲突
        self.bg1.addButton(self.radio1_1)
        self.bg1.addButton(self.radio1_2)
        self.bg1.addButton(self.radio1_3)
        self.layout3.addWidget(QLabel("非互斥radio（使用QButtonGroup: A B）和互斥radio(: C D)"))
        self.layout3.addWidget(self.radio1_1)
        self.layout3.addWidget(self.radio1_2)
        self.layout3.addWidget(self.radio1_3)
        self.layout3.addWidget(self.radio1_4)
        # 查看指定button对应的id
        print(self.bg1.id(self.radio1_1))  # -2
        # 设置指定按钮的id
        self.bg1.setId(self.radio1_1, 1)
        print(self.bg1.id(self.radio1_1))  # 1
        # 查看指定id对应的button
        print(self.bg1.button(-3))
        # 查看QButtonGroup所包含的所有button
        print(self.bg1.buttons())
        # 设置按钮不独占
        self.bg1.setExclusive(False)
        print(self.bg1.exclusive())
        # 移除QButtonGroup中包含的按钮，使其不受影响
        # 结果为：
        # C和D成为一组按钮组（默认成为了独占按钮组，没有用手动设置）
        # A何B成为一组按钮组（因为设置了不独占，所以A和B为非独占按钮组）
        self.bg1.removeButton(self.radio1_3)
        self.layout().addLayout(self.layout3)

        self.layout4 = QHBoxLayout()
        self.bg2 = QButtonGroup(self)
        self.bg2.setExclusive(False)
        self.check2_1 = QCheckBox("A", self)
        self.check2_2 = QCheckBox("B", self)
        self.check2_3 = QCheckBox("C", self)
        self.bg2.addButton(self.check2_1, 1)
        self.bg2.addButton(self.check2_2, 2)
        self.bg2.addButton(self.check2_3, 3)
        self.layout4.addWidget(QLabel("checkbox-使用QButtonGroup-信号连接槽"))
        self.layout4.addWidget(self.check2_1)
        self.layout4.addWidget(self.check2_2)
        self.layout4.addWidget(self.check2_3)

        # 信号连接，事件处理
        self.bg2.buttonClicked.connect(self.button_click)
        # 单击给定按钮时会发出此信号。当一个按钮被第一次按下然后释放，当它的快捷键被输入，
        # 或者当QAbstractButton::click () 或QAbstractButton::animateClick () 被编程调用时，它被点击。
        self.bg2.buttonPressed.connect(self.button_press)
        # 略
        self.bg2.buttonReleased.connect(self.button_release)
        # 略
        self.bg2.buttonToggled.connect(self.button_toggle)
        # 按钮切换时发出该信号，如果按钮被选中， checked为真，如果按钮未被选中，则为假。
        self.bg2.idClicked.connect(self.id_click)
        # 当单击具有给定id的按钮时，会发出此信号。
        self.bg2.idPressed.connect(self.id_press)
        # 略
        self.bg2.idReleased.connect(self.id_release)
        # 略
        self.bg2.idToggled.connect(self.id_toggle)
        # 当具有给定id的按钮被切换时，会发出此信号。如果按钮被选中， checked为真，如果按钮未被选中，则为假。

        self.layout().addLayout(self.layout4)

    @Slot(QAbstractButton)
    def button_click(self, button):
        print("button click", button.text())

    @Slot(QAbstractButton)
    def button_press(self, button):
        print("button press", button.text())

    @Slot(QAbstractButton)
    def button_release(self, button):
        print("button release", button.text())

    # https://doc.qt.io/qtforpython/tutorials/basictutorial/signals_and_slots.html
    # Slot的多参数应该是这样的
    @Slot(QAbstractButton, bool)
    def button_toggle(self, button, state):
        print("button toggle", button, state)

    def id_click(self):
        pass

    def id_press(self):
        pass

    def id_release(self):
        pass

    def id_toggle(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
