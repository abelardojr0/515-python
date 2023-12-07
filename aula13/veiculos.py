class Veiculo:
    def __init__(self, modelo:str, cor:str, ano:int):
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,novo_valor):
        self.__modelo = novo_valor
        return self.__modelo
    

    def getCor(self):
        return self.__cor
    
    def setCor(self,novo_valor):
        self.__cor = novo_valor
        return self.__cor


    def getAno(self):
        return self.__ano
    
    def setAno(self,novo_valor):
        self.__ano = novo_valor
        return self.__ano




    def buzinar(self):
        return "Som indefinido"

class Carro(Veiculo):
    def __init__(self, modelo: str, cor: str, ano: int):
        super().__init__(modelo, cor, ano)
    
    def buzinar(self):
        return "Bi bi"

class Navio(Veiculo):
    def __init__(self, modelo: str, cor: str, ano: int):
        super().__init__(modelo, cor, ano)
    
    def buzinar(self):
        return "Fommmm"
    
class Aviao(Veiculo):
    def __init__(self, modelo: str, cor: str, ano: int):
        super().__init__(modelo, cor, ano)


carro1 = Carro(modelo="HB20", cor="Branco", ano=2022 )
navio1 = Navio(modelo="Titanic", cor="Branco Gelo", ano=1920 )
aviao1 = Aviao(modelo="Boing", cor="Branco", ano=2010 )

# print(carro1.__modelo)
# carro1.__modelo = "Uno"
carro1.setModelo("Uno")
print(carro1.getModelo())


print(carro1.buzinar())
print(navio1.buzinar())
print(aviao1.buzinar())