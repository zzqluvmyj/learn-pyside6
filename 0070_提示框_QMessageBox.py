import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt

"""
QMessageBox 类提供了一个模式对话框，用于通知用户或询问用户问题并接收答案

消息框显示主要文本以提醒用户注意某种情况，显示信息文本以进一步解释警报或询问用户问题，以及可选的详细文本以在用户请求时提供更多数据。消息框还可以显示图标和标准按钮以接受用户响应。

提供了两个使用 QMessageBox 的 API，基于属性的 API 和静态函数。调用其中一个静态函数是一种更简单的方法，但它不如使用基于属性的 API 灵活，结果信息量也更少。建议使用基于属性的 API。
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()

    m = QMessageBox()

    # 第二个参数类型是QMessageBox.ButtonRole，更多有
    # QMessageBox::InvalidRole	-1	按钮无效。
    # QMessageBox::AcceptRole	0	单击该按钮会导致对话框被接受（例如确定）。
    # QMessageBox::RejectRole	1	单击该按钮会导致对话框被拒绝（例如，取消）。
    # QMessageBox::DestructiveRole	2	单击按钮会导致破坏性更改（例如丢弃更改）并关闭对话框。
    # QMessageBox::ActionRole	3	单击该按钮会导致对话框中的元素发生变化。
    # QMessageBox::HelpRole	4	可以单击该按钮来请求帮助。
    # QMessageBox::YesRole	5	该按钮是类似“是”的按钮。
    # QMessageBox::NoRole	6	该按钮是类似“否”的按钮。
    # QMessageBox::ApplyRole	8	该按钮应用当前更改。
    # QMessageBox::ResetRole	7	该按钮将对话框的字段重置为默认值。
    m.addButton("确定", QMessageBox.AcceptRole)

    # QMessageBox.Cancel是带有ButtonRole的预置按钮，更多有
    # QMessageBox::Ok	0x00000400	使用AcceptRole定义的“确定”按钮。
    # QMessageBox::Open	0x00002000	使用AcceptRole定义的“打开”按钮。
    # QMessageBox::Save	0x00000800	使用AcceptRole定义的“保存”按钮。
    # QMessageBox::Cancel	0x00400000	使用RejectRole定义的“取消”按钮。
    # QMessageBox::Close	0x00200000	使用RejectRole定义的“关闭”按钮。
    # QMessageBox::Discard	0x00800000	一个“放弃”或“不保存”按钮，取决于平台，使用DestructiveRole定义。
    # QMessageBox::Apply	0x02000000	使用ApplyRole定义的“应用”按钮。
    # QMessageBox::Reset	0x04000000	使用ResetRole定义的“重置”按钮。
    # QMessageBox::RestoreDefaults	0x08000000	使用ResetRole定义的“恢复默认值”按钮。
    # QMessageBox::Help	0x01000000	使用HelpRole定义的“帮助”按钮。
    # QMessageBox::SaveAll	0x00001000	使用AcceptRole定义的“全部保存”按钮。
    # QMessageBox::Yes	0x00004000	使用YesRole定义的“是”按钮。
    # QMessageBox::YesToAll	0x00008000	使用YesRole定义的“全部同意”按钮。
    # QMessageBox::No	0x00010000	使用NoRole定义的“否”按钮。
    # QMessageBox::NoToAll	0x00020000	使用NoRole定义的“拒绝所有人”按钮。
    # QMessageBox::Abort	0x00040000	使用RejectRole定义的“中止”按钮。
    # QMessageBox::Retry	0x00080000	使用AcceptRole定义的“重试”按钮。
    # QMessageBox::Ignore	0x00100000	使用AcceptRole定义的“忽略”按钮。
    # QMessageBox::NoButton	0x00000000	无效的按钮。
    cancel = QMessageBox.Cancel
    m.addButton(cancel)

    # 设置默认按钮
    m.setDefaultButton(cancel)

    # 设置默认退出按钮，和ESC绑定
    m.setEscapeButton(cancel)

    # 所有的按钮
    print(m.buttons())

    # 设置详细文本
    m.setDetailedText("详细文本")

    # QMessageBox 支持四种预定义的消息严重性级别或消息类型
    # 通过将icon属性设置为预定义图标之一来指定四种预定义消息类型之一
    # 这4个图标对应于QMessageBox的四个静态方法
    # 设置图标后有声音
    # QMessageBox::NoIcon	0	消息框没有任何图标。
    # QMessageBox::Question	4	一个图标，表示消息正在提问。
    # QMessageBox::Information	1	一个图标，表示该消息没有异常。
    # QMessageBox::Warning	2	一个图标，表示消息是警告，但可以处理。
    # QMessageBox::Critical	3	一个图标，表示该消息代表一个严重问题。
    # 也可以使用setIconPixmap设置自己的图标
    m.setIcon(QMessageBox.Information)

    # 一次性设置多个按钮，而不是通过addButton
    # setStandardButtons(QMessageBox.Save  | QMessageBox.Discard  | QMessageBox.Cancel)

    # 设置显示文本
    m.setText("这是文本")

    # 设置窗口模态，取值有
    # Qt::NonModal	0	该窗口不是模态的，并且不会阻止对其他窗口的输入。
    # Qt::WindowModal	1	该窗口对单个窗口层次结构是模态的，并阻止对其父窗口、所有祖父窗口以及其父窗口和祖父窗口的所有兄弟窗口的输入。
    # Qt::ApplicationModal	2	该窗口对应用程序是模态的，并阻止对所有窗口的输入。
    m.setWindowModality(Qt.ApplicationModal)

    # 设置标题
    m.setWindowTitle("标题")

    # 获取点击按钮方法1：适用于StandardButton
    # exec()返回被单击按钮的StandardButtons值。
    if m.exec() == QMessageBox.Cancel:
        print("返回")

    # 获取点击的按钮2：适用于通过addButton添加的按钮
    print(m.clickedButton())

    # QMessageBox的静态方法，如下
    # 除了前两者，其他都有返回值，类似于exec()的返回值
    QMessageBox.about(None, "标题", "文本")
    QMessageBox.aboutQt(None, "Qt信息")
    QMessageBox.critical(None, "标题", "文本", QMessageBox.Save | QMessageBox.Discard)
    QMessageBox.information(None, "标题", "文本", QMessageBox.Save | QMessageBox.Discard)
    QMessageBox.question(None, "标题", "文本", QMessageBox.Save | QMessageBox.Discard)
    QMessageBox.warning(None, "标题", "文本", QMessageBox.Save | QMessageBox.Discard)

    sys.exit(app.exec())
