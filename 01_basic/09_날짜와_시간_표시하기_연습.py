from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, Qt
import sys


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDateTime().currentDateTime()
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon("../data/cat_image.png"))
        self.setWindowTitle("this is a test")
        self.setGeometry(300, 300, 600, 300)
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        print(f"{self.date.toString(Qt.DefaultLocaleLongDate) = }")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = MyApp()
    sys.exit(app.exec())