
import sys
# pyqt5 모듈 import와 위젯 가져오기
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# pyqt5 모듈에서 아이콘 삽입
from PyQt5.QtGui import QIcon
# QtCore의 모듈 QCoreApplication 호출
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      # 아이콘 이미지 지정
      self.setWindowIcon(QIcon('icon.png'))
      # title bar의 name 지정
      self.setWindowTitle('pyqt5 위젯')
      # 스크린에서 지정 위치로 이동 -> 지정 안할 경우 화면 정 가운데 생성
      # self.move(960, 540)
      # 위젯 크기 너비, 높이로 지정
      self.resize(450, 450)
      # 스크린 표시

      # -내부
      btn = QPushButton('Quit', self)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)


      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())