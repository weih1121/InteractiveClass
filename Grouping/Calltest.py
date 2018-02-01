import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from test import Ui_MainWindow

class testUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(testUi, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = testUi()
    ui.show()
    sys.exit(app.exec_())