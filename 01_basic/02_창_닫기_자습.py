# 창 띄우기 + 창 아이콘 설정하기
# + 창 닫기 버튼 만들기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super(MyApp, self).__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("창 닫기 버튼 만들기")
        self.setWindowIcon(QIcon("../data/Qfactory_icon.png"))

        btn_01 = QPushButton("닫기", self)
        btn_02 = QPushButton("또 닫기", self)

        btn_01.setGeometry(100, 100, btn_01.sizeHint().width(), btn_01.sizeHint().height())
        btn_02.setGeometry(200, 100, btn_02.sizeHint().width(), btn_02.sizeHint().height())

        btn_01.clicked.connect(QCoreApplication.instance().quit)
        btn_02.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(300,300, 600, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())