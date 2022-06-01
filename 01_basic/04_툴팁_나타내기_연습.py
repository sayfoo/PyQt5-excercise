# 스스로 해야징... 하나 둘 하나 둘...

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("이번에도 연습입니다.")
        self.setWindowIcon(QIcon("../data/web.png"))
        self.setGeometry(300, 300, 600, 300)

        btn = QPushButton("닫기", self)
        btn.setToolTip("This is a <b>Push</b> button.")
        btn.setGeometry(100, 100, btn.sizeHint().width(), btn.sizeHint().height())
        btn.clicked.connect(QCoreApplication.instance().quit)
        print(dir(btn.clicked))

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
