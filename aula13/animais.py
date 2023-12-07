class Animal:
    def __init__(self, nome, raca, especie, cor):
        self.nome = nome
        self.raca = raca
        self.especie = especie
        self.cor = cor
    
    def emitir_som(self):
        return "Som indefinido"

class Cachorro(Animal):
    def __init__(self, nome, raca, especie, cor):
        super().__init__(nome, raca, especie, cor)
    
    def emitir_som(self):
        return "au au"

class Gato(Animal):
    def __init__(self, nome, raca, especie, cor):
        super().__init__(nome, raca, especie, cor)
    
    def emitir_som(self):
        return "Miauuuuuuu"
    
class Camelo(Animal):
    def __init__(self, nome, raca, especie, cor):
        super().__init__(nome, raca, especie, cor)


gato1 = Gato(nome="Cleber", raca="Pé duro", especie="felino", cor="preto")
cachorro1 = Cachorro(nome="Cleiton", raca="Vira lata", especie="Indefinido", cor="Caramelo")
camelo1 = Camelo(nome="Habibi", raca="Dos grandao", especie="Sei la", cor="Marrozim")


print(gato1.emitir_som())
print(cachorro1.emitir_som())
print(camelo1.emitir_som())