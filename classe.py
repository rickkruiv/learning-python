class Computador:
    def __init__(self, marca, memoria_ram, placa_de_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_de_video
        
    def Ligar(self):
        print('Estou ligado')
    
    def Desligar(self):
        print('Estou desligado')
    
    def ExibirInformaçoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus', '16gb', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformaçoesDesteComputador()