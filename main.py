from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.uic import loadUi
from google_map import googleMap
import sys

class Form(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('form.ui', self)

        # 콤보박스 초기화
        #for i in range(1, 21):
        #    self.cmb.addItem(str(i))

        n = [str(i+1) for i in range(20)]
        self.cmb.addItems(n)

        types = ('roadmap', 'satellite', 'terrain', 'hybrid')
        self.map.addItems(types)

        # 시그널
        self.btn.clicked.connect(self.clickBtn)

    def clickBtn(self):
        place = self.le.text()
        w = self.pic.width()
        h = self.pic.height()
        z = self.cmb.currentText()
        t = self.map.currentText()
        img = googleMap(place, w, h, z, t)
        self.pic.setPixmap(img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
