from PyQt5.QtWidgets import QPushButton, QCheckBox, QWidget, QVBoxLayout



class CustomWidget(QWidget):
    def __init__(self, title, parent):
        super(CustomWidget, self).__init__(parent=None)
        self.initUI(title)

    def initUI(self, title):
        layout = QVBoxLayout()
        self.button = QPushButton(self)
        self.button.setStyleSheet("QPushButton{border-image:url(../images/nullImage.jpg);}")
        self.button.setFixedSize(100, 100)
        self.checkBox = QCheckBox(title, self)
        self.checkBox.setCheckable(False)
        self.button.setMinimumSize(100, 100)

        layout.addWidget(self.button)
        layout.addWidget(self.checkBox)
        self.setLayout(layout)


    def close(self):
        self.button.close()
        self.checkBox.close()