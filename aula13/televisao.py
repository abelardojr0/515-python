class Televisao:
    def __init__(self, nome:str, genero:str) :
        self.nome = nome
        self.genero = genero

    def assitir(self):
        return f"O {self.nome} está sendo assistido"

class Filme(Televisao):
    def __init__(self, nome: str, genero: str, duracao:int):
        super().__init__(nome, genero)
        self.duracao = duracao

    def em_cartaz(self):
        return f"O filme {self.nome} está em cartaz"
    
    def assitir(self):
        return f"O filme {self.nome} está sendo assistido agora"

class Serie(Televisao):
    def __init__(self, nome: str, genero: str, num_temporadas:int):
        super().__init__(nome, genero)
        self.num_temporadas = num_temporadas
    
    def maratonar(self):
        return f"A série {self.nome} está sendo maratonada"


nome_filme = str(input("Digite o nome do filme: "))
genero_filme = str(input("Digite o gênero do filme: "))
duracao_filme = int(input("Digite a duração do filme: "))

filme1 = Filme(nome=nome_filme, genero=genero_filme, duracao=duracao_filme)

print(filme1.em_cartaz())
print(filme1.assitir())

nome_serie = str(input("Digite o nome da série: "))
genero_serie = str(input("Digite o gênero da série: "))
temporadas_serie = int(input("Digite a quantidade de temporadas da série: "))

serie1 = Serie(nome=nome_serie, genero=genero_serie, num_temporadas=temporadas_serie)

print(serie1.maratonar())
print(serie1.assitir())

