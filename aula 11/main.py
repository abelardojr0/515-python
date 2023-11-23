class Carro:
  def __init__(self, marca,modelo,ano ):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.velocidade_atual = 0

  def ligar(self):
    return f"O {self.modelo} está ligado"

  def acelerar(self, velocidade):
    self.velocidade_atual = self.velocidade_atual + velocidade
    return self.velocidade_atual
  
  def freiar(self):
    if self.velocidade_atual <= 20:
      self.velocidade_atual = 0
    else:
      self.velocidade_atual = self.velocidade_atual - 20
    return self.velocidade_atual
  
  def desligar(self):
    return f"O {self.modelo} está desligado"
  

  
carro1 = Carro(marca="Hyundai", modelo="HB20", ano=2019)

while True:
  menu = int(input("""
            1 - Ligar
            2 - Acelerar
            3 - Freiar
            4 - Desligar
            0 - Sair
  """))
  match menu:
    case 1:
      print(carro1.ligar())
    case 2:
      velocidade = int(input("Digite o quanto você quer acelerar: "))
      carro1.acelerar(velocidade)
    case 3:
      carro1.freiar()
    case 4:
      carro1.desligar()
    case 0:
      break
    case _:
      print("Opção inválida")

  print(f"Velocidade atual: {carro1.velocidade_atual}")
  
