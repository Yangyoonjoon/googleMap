from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.uic import loadUi
from google_map import googleMap
import sys

class Form(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('form.ui', self)

        # 시그널
        self.btn.clicked.connect(self.clickBtn)

    def clickBtn(self):
        place = self.le.text()
        w = self.pic.width()
        h = self.pic.height()
        img = googleMap(place, w, h)
        self.pic.setPixmap(img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
