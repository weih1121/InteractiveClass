import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CustomWidget import CustomWidget
from group import Ui_MainWindow


class Grouping(QMainWindow, Ui_MainWindow):
    CustomWidgetList = []                                                       #定义一个列表，用来存储学生列表中CustomWidget的控件
    Student_list = {}
    def __init__(self):
        super(Grouping, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gLayout = QGridLayout(self.ui.scrollAreaWidgetContents_studentList)

        self.ui.spinBox_row.valueChanged.connect(self.UpdateWin)                #spinBox值改变触发更新窗口函数
        self.ui.spinBox_col.valueChanged.connect(self.UpdateWin)

        self.ui.pushButton_grouping.pressed.connect(self.HandleButtonContral)   #分组控制信号与对应的槽函数
        self.ui.spinBox_groupNum.valueChanged.connect(self.addGroupNum)

        self.setWindowTitle("设置分组")

        self.RightToolBar = QToolBar('ToolBar')  # 增加一个右侧的ToolBar
        self.RightToolBar.setIconSize(QSize(30, 30))  # 将ToolBar的图标设置成30 * 30
        self.addToolBar(Qt.RightToolBarArea, self.RightToolBar)  # 将ToolBar添加上去

        self.actionbroswer = QAction('Browser')  # 设置浏览器bar
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/ie.png'), QIcon.Normal, QIcon.Off)
        self.actionbroswer.setIcon(icon)
        self.actionbroswer.setObjectName("actionbroswer")
        self.RightToolBar.addAction(self.actionbroswer)

        self.actionscreen = QAction('Scren')  # 设置共享屏幕
        icon =  QIcon()
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

        self.actionchat = QAction("Chat")  # 设置chat
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/penguin.png'), QIcon.Normal, QIcon.Off)
        self.actionchat.setIcon(icon)
        self.actionchat.setObjectName("Chat")
        self.RightToolBar.addAction(self.actionchat)

        self.actionchat = QAction("Chat")  # 设置录屏
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

        self.actionclass = QAction("Class")  # 设置分组
        icon = QIcon()
        icon.addPixmap(QPixmap('../images/toolBarIcon/about.png'), QIcon.Normal, QIcon.Off)
        self.actionclass.setIcon(icon)
        self.actionclass.setObjectName("SnapShot")
        self.RightToolBar.addAction(self.actionclass)

    def UpdateWin(self):
        row = self.ui.spinBox_row.value()
        col = self.ui.spinBox_col.value()

        if self.CustomWidgetList != None:                                       #更新窗口前如果窗口内已经有控件则先将窗口内控件清空
            for widgets in self.CustomWidgetList:
                widgets.close()
        self.CustomWidgetList.clear()

        positions = [(i, j) for i in range(row) for j in range(col)]
        names = []
        for x in range(row * col):
            names.append("Student" + str(x + 1))

        for position, name in zip(positions, names):
            widget = CustomWidget(name, self.gLayout)
            self.gLayout.addWidget(widget, *position)
            self.CustomWidgetList.append(widget)

    def HandleButtonContral(self):
        for widget in self.CustomWidgetList:
            widget.checkBox.setCheckable(True)

    def addGroupNum(self):
        self.ui.comboBox_group.clear()
        num = self.ui.spinBox_groupNum.value()
        for x in range(num):
            self.ui.comboBox_group.addItem("第{0}组".format(x + 1))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Grouping()
    win.show()
    sys.exit(app.exec_())
