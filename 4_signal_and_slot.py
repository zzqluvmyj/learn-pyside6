# 由于 Qt 的性质，QObjects 需要一种通信方式，这就是这种机制成为Qt 核心特性的原因。

# 简单来说，您可以像与家里的灯互动一样理解Signal 和 Slots 。当您移动电灯开关（信号）时，您会得到一个结果，可能是您的灯泡打开/关闭（插槽）。

# 在开发界面时，您可以通过单击按钮的效果来获得一个真实的示例：“单击”将是信号，而插槽将是单击该按钮时发生的情况，例如关闭窗口，保存文档等.

# 所有继承自QObject其子类或其子类之一的类 QWidget都可以包含信号和插槽。 当对象以可能对其他对象感兴趣的方式改变其状态时，信号由对象发出。这就是对象进行通信的全部内容。它不知道也不关心是否有任何东西在接收它发出的信号。这是真正的信息封装，并确保对象可以用作软件组件。

# 槽可以用来接收信号，但它们也是普通的成员函数。就像一个对象不知道是否有任何东西接收到它的信号一样，一个槽也不知道它是否有任何信号连接到它。这确保了可以使用 Qt 创建真正独立的组件。

# 您可以将任意数量的信号连接到单个插槽，并且可以将信号连接到任意数量的插槽。甚至可以将一个信号直接连接到另一个信号。（这将在第一个信号发出时立即发出第二个信号。）

# Qt 的小部件有许多预定义的信号和槽。例如， QAbstractButton（Qt 中按钮的基类）有一个clicked() 信号，QLineEdit（单行输入字段）有一个名为“clear()”的槽。因此，可以通过在QLineEdit的右侧 放置一个QToolButton并将其clicked()信号连接到插槽“clear()”来实现带有清除文本的按钮的文本输入字段。这是使用信号的connect()方法完成的

# button = QToolButton()
# line_edit = QLineEdit()
# button.clicked.connect(line_edit.clear)

# connect()返回一个QMetaObject.Connection对象，可以与disconnect()方法一起使用来断开连接。

# 信号也可以连接到自由函数：

# import sys
# from PySide6.QtWidgets import QApplication, QPushButton


# def function():
#     print("The 'function' has been called!")

# app = QApplication()
# button = QPushButton("Call function")
# button.clicked.connect(func)
# button.show()
# sys.exit(app.exec())


# 信号类
# 在 Python 中编写类时，信号被声明为 class 的类级变量QtCore.Signal()。发出clicked()信号的基于 QWidget 的按钮可能如下所示：
# from PySide6.QtCore import Qt, Signal
# from PySide6.QtWidgets import QWidget

# class Button(QWidget):

#     clicked = Signal(Qt.MouseButton)

#     ...

#     def mousePressEvent(self, event):
#         self.clicked.emit(event.button())

# Signal构造函数接受一个元组或 Python 类型和 C 类型的列表
# signal1 = Signal(int)  # Python types
# signal2 = Signal(QUrl)  # Qt Types
# signal3 = Signal(int, str, int)  # more than one type
# signal4 = Signal((float,), (QDate,))  # optional types

# 除此之外，它还可以接收name定义信号名称的命名参数。如果没有传递任何内容，则新信号将与分配给它的变量具有相同的名称。
# # TODO
# signal5 = Signal(int, name='rangeChanged')
# # ...
# rangeChanged.emit(...)

# 另一个有用的选项Signal是参数名称，对于 QML 应用程序按名称引用发出的值很有用

# 插槽类
# QObject 派生类中的插槽应由装饰器指示 @QtCore.Slot()。同样，要定义签名，只需传递与QtCore.Signal()相似的类型
# @Slot(str)
# def slot_function(self, s):
#     ...

# Slot()也接受一个name和一个result关键字。result关键字定义将返回的类型，可以是 C 或 Python 类型。关键字的name行为方式与Signal(). 如果没有作为名称传递，则新插槽将与正在修饰的函数具有相同的名称。

# 实际上可以使用具有不同参数类型列表的相同名称的信号和槽。这是 Qt 5 的遗留问题，不推荐用于新代码。在 Qt 6 中，不同类型的信号具有不同的名称。

# 以下示例使用 Signal 和 Slot 的两个处理程序来展示不同的功能。
# 无法运行

# import sys
# from PySide6.QtWidgets import QApplication, QPushButton
# from PySide6.QtCore import QObject, Signal, Slot


# class Communicate(QObject):
#     # create two new signals on the fly: one will handle
#     # int type, the other will handle strings
#     speak = Signal((int,), (str,))

#     def __init__(self, parent=None):
#         super().__init__(self, parent)

#         self.speak[int].connect(self.say_something)
#         self.speak[str].connect(self.say_something)

#     # define a new slot that receives a C 'int' or a 'str'
#     # and has 'say_something' as its name
#     @Slot(int)
#     @Slot(str)
#     def say_something(self, arg):
#         if isinstance(arg, int):
#             print("This is a number:", arg)
#         elif isinstance(arg, str):
#             print("This is a string:", arg)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     someone = Communicate()

#     # emit 'speak' signal with different arguments.
#     # we have to specify the str as int is the default
#     someone.speak.emit(10)
#     someone.speak[str].emit("Hello everybody!")
