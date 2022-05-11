import sys
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QToolButton, QMenu, QWidget
from PySide6.QtCore import Qt

import sys

# 0.创建一个APP
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QToolButton")
w.resize(300, 300)

# 创建菜单
menu = QMenu()
# 创建子菜单
sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("menu.ico"))

# 在菜单中添加子菜单
menu.addMenu(sub_menu)

# 创建action并添加到菜单中
action = QAction(QIcon("menu.ico"), "行为", menu)
menu.addAction(action)
# 响应action点击事件
action.triggered.connect(lambda: print("点击了 action"))


# 创建一个 QToolButton
tb = QToolButton(w)
tb.setText("hell")
tb.setAutoRaise(True)


# QToolBool添加菜单
tb.setMenu(menu)


w.show()

sys.exit(app.exec())
