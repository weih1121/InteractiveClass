from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

from DrawPicture.draw import Draw
from Grouping.grouping import Grouping
from Snapshot.src.screenshot import SnapShot


class MainWindow(QMainWindow):
    # noinspection PyUnresolvedReferences
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('吉林省裕昌恒科技有限公司互动课堂')
        # 设置窗口图标
        self.setWindowIcon(QIcon('images/icons/penguin.png'))
        # 设置窗口大小900*600
        self.resize(800, 600)
        self.show()

        # 设置浏览器
        self.browser = QWebEngineView ()
        #browser = QWebView()
        url = 'https://www.baidu.com'
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)


        ###使用QToolBar创建导航栏，并使用QAction创建按钮
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(16, 16))
        #添加导航栏到窗口中
        self.addToolBar(navigation_bar)

        #QAction类提供了抽象的用户界面action，这些action可以被放置在窗口部件中
        # 添加前进、后退、停止加载和刷新的按钮
        back_button = QAction(QIcon('./icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('./icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('./icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('./icons/renew.png'), 'reload', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        # 将按钮添加到导航栏上
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        #添加URL地址栏
        self.urlbar = QLineEdit()
        # 让地址栏能响应回车按键信号
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)

        #让浏览器相应url地址的变化
        self.browser.urlChanged.connect(self.renew_urlbar)

        self.RightToolBar = QToolBar('ToolBar')  # 增加一个右侧的ToolBar
        self.RightToolBar.setIconSize(QSize(30, 30))  # 将ToolBar的图标设置成30 * 30
        self.addToolBar(Qt.RightToolBarArea, self.RightToolBar)  # 将ToolBar添加上去

        self.actionbroswer = QAction('Browser')  # 设置浏览器bar
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/ie.png'), QIcon.Normal, QIcon.Off)
        self.actionbroswer.setIcon(icon)
        self.actionbroswer.setObjectName("actionbroswer")
        self.RightToolBar.addAction(self.actionbroswer)

        self.actionscreen = QAction('Screen')  # 设置共享屏幕
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/screen.png'), QIcon.Normal, QIcon.Off)
        self.actionscreen.setIcon(icon)
        self.actionscreen.setObjectName("actionscreen")
        self.RightToolBar.addAction(self.actionscreen)

        self.actiondrawboard = QAction("DrawBoard")  # 设置画板
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/huaban.png'), QIcon.Normal, QIcon.Off)
        self.actiondrawboard.setIcon(icon)
        self.actiondrawboard.setObjectName("DrawBoard")
        self.RightToolBar.addAction(self.actiondrawboard)
        self.actiondrawboard.triggered.connect(self.CallDrawPicture)

        self.actionchat = QAction("Chat")  # 设置chat
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/penguin.png'), QIcon.Normal, QIcon.Off)
        self.actionchat.setIcon(icon)
        self.actionchat.setObjectName("Chat")
        self.RightToolBar.addAction(self.actionchat)

        self.actionopenfile = QAction("OpenFile")  # 设置打开文件
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/find.png'), QIcon.Normal, QIcon.Off)
        self.actionopenfile.setIcon(icon)
        self.actionopenfile.setObjectName("Chat")
        self.RightToolBar.addAction(self.actionopenfile)

        self.actionsnapshot = QAction("SnapShot")  # 设置截屏
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/jianqieban.png'), QIcon.Normal, QIcon.Off)
        self.actionsnapshot.setIcon(icon)
        self.actionsnapshot.setObjectName("SnapShot")
        self.RightToolBar.addAction(self.actionsnapshot)
        self.actionsnapshot.triggered.connect(self.CallSnapShot)

        self.actionclass = QAction("Class")  # 设置分组
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/about.png'), QIcon.Normal, QIcon.Off)
        self.actionclass.setIcon(icon)
        self.actionclass.setObjectName("SnapShot")
        self.RightToolBar.addAction(self.actionclass)
        self.actionclass.triggered.connect(self.CallGrouping)


    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar(self, q):
        # 将当前网页的链接更新到地址栏
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def CallDrawPicture(self):
        drawPicture = Draw()
        drawPicture.show()

    def CallGrouping(self):
        group = Grouping()
        group.show()

    def CallSnapShot(self):
        snapshot = SnapShot()
        snapshot.show()

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    window = MainWindow()
    # 显示窗口
    window.show()
    # 运行应用，并监听事件
    app.exec_()
