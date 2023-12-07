class Automovel:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        return f"O {self.modelo} está ligando"

class Moto(Automovel):
    def __init__(self, marca, modelo, ano, cor, cilindradas):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
    
    def empinar(self):
        return f"A moto {self.modelo} está empinando"

class Carro(Automovel):
    def __init__(self, marca, modelo, ano, cor, num_portas):
        super().__init__(marca, modelo, ano, cor)
        self.num_portas = num_portas
    
    def cavalo_de_pau(self):
        return f"O carro {self.modelo} está dando cavalo de pau"
    
moto1 = Moto(marca="honda", modelo= "bros", ano=2020, cor="preto", cilindradas=160)
carro1 = Carro(marca="ford", modelo= "ka", ano=2019, cor="cinza", num_portas=4)


        