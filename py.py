class Mashina:
    def __init__(self, rang, model,tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik
    # metod yaratamiz
    # 1 - metod gaz ber metodi
    def gaz_ber(self, miqdor):
        self.tezlik += miqdor
    # 2 - metod tormozla metodi
    def tormoz(self, miqdor):
        self.tezlik -= miqdor
        if self.tezlik < 0:
            self.tezlik = 0

Gentra = Mashina("Qora", "Gentra", 200)
Nexia = Mashina("Oq", "Nexia", 150)
Nissan = Mashina("Qizil", "Nissan", 270)
Damas = Mashina("Oq", "Damas", 500)
roketa = Mashina("Oq", "Roketa", 100000)

Damas.gaz_ber(50)
Damas.tormoz(400)
print(f"Damas modeli: {Damas.model}, Damas rangi: {Damas.rang}, Damas tezliki: {Damas.tezlik}")
print(roketa.tezlik)