import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placeholder text")
    w.setAlignment(Qt.AlignCenter)  # 居中对齐
    # 设置样式表
    w.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-size: 30px;
    """)
    w.show()
    sys.exit(app.exec())