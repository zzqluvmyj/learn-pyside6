import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

# 因为qml学习资料少，而且没有设计工具，所以不使用这种技术
# 重点在Qwidget，qml知道就行

if __name__ == "__main__":
    app = QApplication()
    view = QQuickView()

    view.setSource("view1.qml")
    view.show()
    sys.exit(app.exec())
