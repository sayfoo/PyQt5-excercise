# setWindowIcon(QIcon("icon.png")
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Application Icon Insertion Practice")
        self.setWindowIcon(QIcon("../data/Qfactory_icon.png"))
        # self.setWindowIcon(QIcon("../data/cat_image.png"))

        self.setGeometry(300,300, 600, 300)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())