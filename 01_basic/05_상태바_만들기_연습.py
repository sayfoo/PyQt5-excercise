# exercise

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QIcon("../data/Qfactory_icon.png"))
        self.setWindowTitle("상태바 나타내기")
        self.setGeometry(300, 300, 600, 300)

        btn = QPushButton("Push Button", self)
        btn.setToolTip("여기는 <b>Push Button</b> 입니다.")
        btn.setGeometry(100, 100, btn.sizeHint().width(), btn.sizeHint().height())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage("상태바")
        self.setToolTip("상태바")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())