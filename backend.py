import json
import socket

from frontend import MyWindowUI


class Client:

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "8.tcp.ngrok.io"
    port = 13961

    def __init__(self):
        while True:
            try:
                self.socket.connect((self.host, self.port))
                print("Connected to server")
                break
            except ConnectionRefusedError:
                print("Connection refused, retrying...")
                continue

    def send(self, message):
        self.socket.send(message.encode())

    def receive(self):
        return self.socket.recv(1024).decode('utf-8')

    def close(self):
        self.socket.close()


class MyWindow(MyWindowUI):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.client = Client()

        self.islem_tamamlama_button.clicked.connect(self.urun_ekle)
        self.urun_bilgilerini_getir_button.clicked.connect(self.urun_bilgilerini_getir)

    def urun_bilgilerini_getir(self):

        self.client.socket.send('get_products'.encode())
        product_list = json.loads(self.client.receive())
        self.acer_model_rslt.setText(product_list[0]['model'])
        self.acer_fiyat_rslt.setText(str(product_list[0]['price']))
        self.acer_screen_rslt.setText(str(product_list[0]['screen_size']))
        self.acer_ram_rslt.setText(str(product_list[0]['ram']))
        self.acer_processor_rslt.setText(product_list[0]['processor'])
        #
        self.apple_model_rslt.setText(product_list[1]['model'])
        self.apple_fiyat_rslt.setText(str(product_list[1]['price']))
        self.apple_screen_rslt.setText(str(product_list[1]['screen_size']))
        self.apple_ram_rslt.setText(str(product_list[1]['ram']))
        self.apple_processor_rslt.setText(product_list[1]['processor'])
        #
        self.lenovo_model_rslt.setText(product_list[2]['model'])
        self.lenovo_fiyat_rslt.setText(str(product_list[2]['price']))
        self.lenovo_screen_rslt.setText(str(product_list[2]['screen_size']))
        self.lenovo_ram_rslt.setText(str(product_list[2]['ram']))
        self.lenovo_processor_rslt.setText(product_list[2]['processor'])
        #
        self.monster_model_rslt.setText(product_list[3]['model'])
        self.monster_fiyat_rslt.setText(str(product_list[3]['price']))
        self.monster_screen_rslt.setText(str(product_list[3]['screen_size']))
        self.monster_ram_rslt.setText(str(product_list[3]['ram']))
        self.monster_processor_rslt.setText(product_list[3]['processor'])

    def urun_ekle(self):
        product_dict = {
            'brand': self.marka_line_edit.text(),
            'model': self.model_line_edit.text(),
            'processor': self.islemci_line_edit.text(),
            'ram': self.ram_line_edit.text(),
            'screen_size': self.ekran_boyutu_line_edit.text(),
            'price': self.fiyat_line_edit.text(),
        }

        self.client.socket.send(json.dumps(product_dict).encode())
        print(self.client.receive())
