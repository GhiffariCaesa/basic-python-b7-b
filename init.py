class hewan:
    def __init__(self, kaki, gigi, makanan):
        self.kaki = kaki
        self.gigi = gigi
        self.makanan = makanan

tiger = hewan(4, "Punya taring", "Daging")
kancil = hewan(4, "Tidak punya taring", "Tumbuhan")
print(tiger.kaki)
print(tiger.gigi)        