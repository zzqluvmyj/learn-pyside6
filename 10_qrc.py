# qrc或者rc是资源文件，例如图片，图标，字体等
# 和ui文件一样，需要转换，命令如下
# pyside6-rcc icons.rc -o rc_icons.py
# 转化后的py文件中保存着二进制数据

import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
import rc_icons  # 不要忘了这个

app = QApplication(sys.argv)
lb1 = QLabel()

lb1.setPixmap(QPixmap(":icons/1.png"))
# lb1.setPixmap(QPixmap(":icons/1.png"))  # 其实可以用相对路径或者绝对路径，不需要qrc文件
lb1.repaint()
lb1.show()


app.exec()
