import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import Qt

# WindowFlags可以设置窗口类型，基本上所有的小部件都有该参数
# 下面以QWidget为例，演示WindowFlags的用法
# 先了解即可，以后还会有特定的例子来进一步说明用法
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # WindowFlags可以在__init__函数中指定（构造函数）
        # 也可以用setWindowFlags()指定WindowFlags
        # 为了方便演示，以下使用setWindowFlags()

        # 查看默认的 WindowFlags
        print(self.windowFlags())

        ###############################
        # 设置WindowFlags

        # QWidget的默认类型。如果它们有父级，这种类型的部件是子部件，如果没有父控件，则为独立窗口
        # self.setWindowFlags(Qt.Widget)

        # 表示小部件是一个窗口，无论窗口小部件是否具有父控件，通常具有窗口系统框架和标题栏。
        # 请注意，如果部件没有父控件，则无法取消设置此标记（可以用在弹出子窗口比父窗口大很多的情况下）
        # self.setWindowFlags(Qt.Window)

        # 指示部件是应该作为对话框窗口（即标题栏中通常没有最大化或最小化按钮）。这是 QDialog 的默认类型。如果要将其用作模态对话框，则应从另一个窗口启动它，
        # 或者如果有父窗口，则与 QWidget::windowModality 属性一起使用。
        # self.setWindowFlags(Qt.Dialog)

        # 表示该窗口是 Macintosh 工作表。 由于使用工作表意味着窗口模态，推荐的方法是使用 QWidget :: setWindowModality() 或 QDialog :: open()。
        # self.setWindowFlags(Qt.Sheet)

        # 表示该窗口小部件是 Macintosh 抽屉。
        # self.setWindowFlags(Qt.Drawer)

        # 表示窗口小部件是弹出式顶级窗口，即它是模态的，但具有适合弹出菜单的窗口系统框架
        # self.setWindowFlags(Qt.Popup)

        # 表示窗口小部件是工具窗口。工具窗口通常是一个小窗口，其标题栏和装饰比通常小，通常用于工具按钮的集合。
        # 如果有父部件，则工具窗口将始终保持在其上。
        # 如果没有父部件，您可以考虑使用 Qt :: WindowStaysOnTopHint 使其位于最顶端。
        # 默认情况下，当应用程序处于非活动状态时，工具窗口将消失。
        # 这可以通过 Qt :: WA_MacAlwaysShowToolWindow 属性来控制。
        # self.setWindowFlags(Qt.Tool)

        # 表示窗口小部件是工具提示。 这在内部用于实现工具提示，没有标题栏和窗口边框。
        # self.setWindowFlags(Qt.ToolTip)

        # 表示该窗口是闪屏。 这是 QSplashScreen 的默认类型。
        # self.setWindowFlags(Qt.SplashScreen)

        # 表示此小组件是桌面。 这是 QDesktopWidget 的类型。
        # self.setWindowFlags(Qt.Desktop)

        # 表示此窗口小部件是子窗口，例如 QMdiSubWindow 窗口小部件。
        # self.setWindowFlags(Qt.SubWindow)

        # 指示此窗口对象是表示由另一个进程创建的本机平台窗口或手动使用本机代码的句柄。
        # self.setWindowFlags(Qt.ForeignWindow)

        # 表示该窗口代表一个封面窗口，例如，当应用程序在 BlackBerry 平台上最小化时显示。
        # self.setWindowFlags(Qt.CoverWindow)

        #####################
        # 以下WindowFlags可以自定义顶级窗口的外观，对其他窗口没有影响

        # 在 Windows 上为窗口提供一个细对话框边框。这种风格传统上用于固定大小的对话框。
        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

        # 在 Windows 上为窗口提供自己的显示上下文。
        # self.setWindowFlags(Qt.MSWindowsOwnDC)

        # 此标志可用于向平台插件指示应禁用“所有”窗口管理器协议。根据应用程序运行的操作系统和窗口管理器运行的情况，该标志的行为会有所不同。该标志可用于获取未设置配置的本机窗口。
        # self.setWindowFlags(Qt.BypassWindowManagerHint)

        # 完全绕过窗口管理器。这会导致一个完全不受管理的无边框窗口（即，除非您手动调用QWidget::activateWindow ()，否则没有键盘输入）。
        # self.setWindowFlags(Qt.X11BypassWindowManagerHint)

        # 生成无边框窗口。用户不能通过窗口系统移动或调整无边框窗口的大小。在 X11 上，标志的结果取决于窗口管理器及其理解 Motif 和/或 NETWM 提示的能力。大多数现有的现代窗口管理器都可以处理这个问题。
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # 禁用支持平台上的窗口投影。
        # self.setWindowFlags(Qt.NoDropShadowWindowHint)

        # CustomizeWindowHint标志用于启用窗口控件的自定义。必须设置此标志以允许更改WindowTitleHint、WindowSystemMenuHint、WindowMinimizeButtonHint、WindowMaximizeButtonHint、WindowCloseButtonHint
        # CustomizeWindowHint关闭默认窗口标题提示。
        self.setWindowFlags(Qt.CustomizeWindowHint)

        # 给窗口一个标题栏。
        self.setWindowFlags(Qt.WindowTitleHint)

        # 添加一个窗口系统菜单，可能还有一个关闭按钮（例如在 Mac 上）。
        # 如果需要隐藏或显示关闭按钮，使用WindowCloseButtonHint起来更便携。
        self.setWindowFlags(Qt.WindowSystemMenuHint)

        # 添加一个最小化按钮。在某些平台上，这意味着 Qt::WindowSystemMenuHint 可以正常工作。
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)

        # 添加最大化按钮。在某些平台上，这意味着 Qt::WindowSystemMenuHint 可以正常工作。
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

        # 添加最小化和最大化按钮。在某些平台上，这意味着 Qt::WindowSystemMenuHint 可以正常工作。
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)

        # 添加关闭按钮。在某些平台上，这意味着 Qt::WindowSystemMenuHint 可以正常工作。
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 向对话框添加上下文帮助按钮。在某些平台上，这意味着 Qt::WindowSystemMenuHint 可以正常工作。
        self.setWindowFlags(Qt.WindowContextHelpButtonHint)

        # 在 macOS 上添加了一个工具栏按钮（即，位于具有工具栏的窗口右上角的长方形按钮）。
        self.setWindowFlags(Qt.MacWindowToolBarButtonHint)

        # 在 macOS 上添加了一个全屏按钮。
        self.setWindowFlags(Qt.WindowFullscreenButtonHint)

        # 如果父窗口小部件已经嵌入，则防止窗口及其子窗口自动将自己嵌入到QGraphicsProxyWidget中。
        # 如果您希望小部件始终是桌面上的顶级小部件，则可以设置此标志，无论父小部件是否嵌入场景中。
        self.setWindowFlags(Qt.BypassGraphicsProxyWidget)

        # 如果底层窗口管理器支持，则添加一个阴影按钮来代替最小化按钮。
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 通知窗口系统该窗口应位于所有其他窗口的底部。
        self.setWindowFlags(Qt.WindowStaysOnBottomHint)

        # 通知窗口系统该窗口仅用于输出（显示某些内容），不接受输入。因此，输入事件应该像不存在一样通过。
        self.setWindowFlags(Qt.WindowTransparentForInput)

        # 通知窗口系统该窗口实现了它自己的一组手势，并且系统级手势，例如三指桌面切换，应该被禁用。
        self.setWindowFlags(Qt.WindowOverridesSystemGestures)

        # 通知窗口系统该窗口不应接收输入焦点。
        self.setWindowFlags(Qt.WindowDoesNotAcceptFocus)

        # 通知窗口系统在最大化窗口时应该尽可能多地使用可用的屏幕几何图形，包括可能被系统 UI 覆盖的区域，例如状态栏或应用程序启动器。
        # 这可能会导致窗口被放置在这些系统 UI 下，但并不保证，具体取决于平台是否支持。
        # 当启用该标志时，用户负责将QScreen::availableGeometry () 考虑在内，以便应用程序中需要用户交互的任何 UI 元素都不会被系统 UI 覆盖。
        self.setWindowFlags(Qt.MaximizeUsingFullscreenGeometryHint)

        # 用于提取窗口标志的窗口类型部分的掩码。
        # Qt.WindowType_Mask

        #####################
        # 多个WindowFlags用|连接 如下所示
        # self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        # 取消某个 WindowFlags 如下所示
        # self.setWindowFlags(self.WindowFlags() & ~Qt.CustomizeWindowHint)
        # 判断是否设置了某个 WindowFlags 如下所示
        # (self.WindowFlags() | Qt.CustomizeWindowHint) == self.WindowFlags()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    app.exec()
