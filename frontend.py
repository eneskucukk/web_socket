import sys

from PyQt5.QtWidgets import QMainWindow

from mainwindow import Ui_MainWindow


class MyWindowUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindowUI, self).__init__()
        self.setupUi(self)
        self.marka_line_edit.setPlaceholderText("Marka Giriniz")
        self.model_line_edit.setPlaceholderText("Model Giriniz")
        self.islemci_line_edit.setPlaceholderText("İşlemci Giriniz")
        self.ram_line_edit.setPlaceholderText("Ram Boyutu Giriniz")
        self.ekran_boyutu_line_edit.setPlaceholderText("Ekran Boyutu Giriniz")
        self.fiyat_line_edit.setPlaceholderText("Fiyat Bilgisi Giriniz")
        self.acer_button.clicked.connect(self.acer_button_clicked)
        self.apple_button.clicked.connect(self.apple_button_clicked)
        self.lenovo_button.clicked.connect(self.lenovo_button_clicked)
        self.monster_button.clicked.connect(self.monster_button_clicked)
        self.urun_ekleme_button.clicked.connect(self.urun_ekleme_button_clicked)
        self.islem_tamamlama_button.clicked.connect(self.islem_tamamlama_button_clicked)

    def acer_button_clicked(self):
        self.monster_button.setStyleSheet("color: white;")
        self.apple_button.setStyleSheet("color: white;")
        self.lenovo_button.setStyleSheet("color: white;")
        self.acer_button.setStyleSheet("color: red;")
        self.islem_tamamlama_button.setStyleSheet("color: white;")
        self.stackedWidget.setCurrentIndex(0)

    def apple_button_clicked(self):
        self.acer_button.setStyleSheet("color: white;")
        self.monster_button.setStyleSheet("color: white;")
        self.lenovo_button.setStyleSheet("color: white;")
        self.apple_button.setStyleSheet("color: red;")
        self.islem_tamamlama_button.setStyleSheet("color: white;")
        self.stackedWidget.setCurrentIndex(1)

    def lenovo_button_clicked(self):
        self.acer_button.setStyleSheet("color: white;")
        self.apple_button.setStyleSheet("color: white;")
        self.monster_button.setStyleSheet("color: white;")
        self.lenovo_button.setStyleSheet("color: red;")
        self.islem_tamamlama_button.setStyleSheet("color: white;")
        self.stackedWidget.setCurrentIndex(2)

    def monster_button_clicked(self):
        self.acer_button.setStyleSheet("color: white;")
        self.apple_button.setStyleSheet("color: white;")
        self.lenovo_button.setStyleSheet("color: white;")
        self.monster_button.setStyleSheet("color: red;")
        self.islem_tamamlama_button.setStyleSheet("color: white;")
        self.stackedWidget.setCurrentIndex(3)

    def urun_ekleme_button_clicked(self):
        self.stackedWidget.setCurrentIndex(4)

    def islem_tamamlama_button_clicked(self):
        self.islem_tamamlama_button.setStyleSheet("color: red;")
