class person:
    def __init__(self, input_nama, input_umur, input_tinggi, input_hobi):
        self.nama = input_nama
        self.umur = input_umur
        self.tinggi = input_tinggi
        self.hobi = input_hobi
    def greet(self):
        print("Nama saya adalah",self.nama,"saat ini saya berumur",self.umur,"saya saat ini memeliki tinggi",self.tinggi,"cm")

user = person("Ghiffari", 21, 168, "Membaca buku")
user.greet()        