class Cachorro:
  def __init__(self, nome, raca, idade, cor, adestrado):
      self.nome = nome
      self.raca = raca
      self.idade = idade
      self.cor = cor
      self.adestrado = adestrado
  def comer(self):
     return f"O {self.nome} está comendo."
  def dormir(self):
     return f"O {self.nome} está dormindo."

cachorrim = Cachorro(nome="Abelardo", raca="Vira lata", idade=2, cor="Sujo", adestrado=False)

print(cachorrim.comer())
print(cachorrim.dormir())

    