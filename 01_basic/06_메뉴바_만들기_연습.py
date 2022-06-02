import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QIcon("../data/web.png"))
        self.setWindowTitle("메뉴바 만들기 연습")
        self.setGeometry(300, 300, 600, 300)

        exit_action = QAction(QIcon("../data/cat_image.png"), "exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(exit_action)

        self.statusBar().showMessage("Hello~")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())