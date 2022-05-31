# 창을 닫는 가장 간단한 방법은 타이틀바의 오른쪽 (Windows) 또는 왼쪽 (macOS) 'X' 버튼을 클릭하는 것입니다.
# 이번에는 프로그래밍을 통해 창을 닫는 법을 알아보겠습니다.
# 시그널 (Signal)과 슬롯 (Slot)에 대해서도 간단하게 다뤄보겠습니다.

## Ex 3-3. 창 닫기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication, QSize


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self)
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      print(f"{btn.sizeHint() = }")
      x = btn.sizeHint()
      print(f"{x.width() =} , {x.height() = }")
      btn.clicked.connect(QCoreApplication.instance().quit)

      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())