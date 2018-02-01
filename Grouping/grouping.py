import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
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
