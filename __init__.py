import sys

from PyQt5.QtWidgets import QApplication

from backend import MyWindow

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
