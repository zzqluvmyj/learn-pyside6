import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)
from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCharFormat

"""
void	copyAvailable(bool yes)
void	currentCharFormatChanged(const QTextCharFormat &f)
void	cursorPositionChanged()
void	redoAvailable(bool available)
void	selectionChanged()
void	textChanged()
void	undoAvailable(bool available)
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.text_edit.copyAvailable.connect(self.copy_available)
        self.text_edit.currentCharFormatChanged.connect(
            self.current_char_format_changed
        )
        self.text_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.text_edit.redoAvailable.connect(self.redo_available)
        self.text_edit.selectionChanged.connect(self.selection_changed)
        self.text_edit.textChanged.connect(self.text_change)
        self.text_edit.undoAvailable.connect(self.undo_available)

    @Slot(bool)
    def copy_available(self, yes: bool) -> None:
        print("copy_available", yes)

    @Slot(QTextCharFormat)
    def current_char_format_changed(self, f: QTextCharFormat) -> None:
        print("current_char_format_changed", f)

    @Slot()
    def cursor_position_changed(self):
        print("cursor_position_changed")

    @Slot(bool)
    def redo_available(self, available: bool) -> None:
        print("redo_available", available)

    @Slot()
    def selection_changed(self):
        print("selection_changed")

    @Slot()
    def text_change(self):
        print("text_change")

    @Slot(bool)
    def undo_available(self, available: bool) -> None:
        print("undo_available", available)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
