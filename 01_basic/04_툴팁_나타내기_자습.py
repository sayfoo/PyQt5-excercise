import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super(MyApp, self).__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("툴팁 나타내기")
        self.setGeometry(300, 300, 600, 300)

        # QToolTip.setFont(QFont("SansSerif", 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton("Quit", self)
        btn.setGeometry(100, 100, btn.sizeHint().width(), btn.sizeHint().height())
        btn.setToolTip('This is a <b>QWidget</b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())