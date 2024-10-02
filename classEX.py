class Carro:
    def __init__(self, marca, preco, motor):
        self.marca = marca
        self.preco = preco
        self.motor = motor
    
    def Tanque(self):
        print('Tanque cheio')
    
    def InfoCarr(self):
        print(self.marca, self.preco, self.motor)
    
    def Trancao(self):
        print('Tração 4x4')

carro = Carro('BMW', 'R$568.99', 'V8')
carro.Trancao()
carro.Tanque()
carro.InfoCarr()