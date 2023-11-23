class Jogo:
  def __init__(self, nome:str, ano: int, genero: str, preco:float, estoque:bool):
    self.nome = nome
    self.ano = ano
    self.genero = genero
    self.preco = preco
    self.estoque = estoque

jogo1 = Jogo(nome= "League of Legends", ano=2010, genero="MOBA", preco=0, estoque=True)

if jogo1.estoque == True:
  print(f"O jogo {jogo1.nome} tem em estoque")
else:
  print(f"O jogo {jogo1.nome} não tem em estoque")

if jogo1.preco > 300:
  print(f"O jogo {jogo1.nome} é muito caro, quero não")
else:
  print(f"O jogo {jogo1.nome} ta baratim, me dê papai")

nome = str(input("Digite o nome do jogo: "))
ano = int(input("Digite o ano do jogo: "))
genero = str(input("Digite o gênero do jogo: "))
preco = float(input("Digite o preço do jogo: "))
estoque = bool(input("O jogo tem em estoque?: "))

jogo2 = Jogo(nome=nome, ano=ano, genero=genero, preco=preco, estoque=estoque)


if jogo2.estoque == True:
  print(f"O jogo {jogo2.nome} tem em estoque")
else:
  print(f"O jogo {jogo2.nome} não tem em estoque")

if jogo2.preco > 300:
  print(f"O jogo {jogo2.nome} é muito caro, quero não")
else:
  print(f"O jogo {jogo2.nome} ta baratim, me dê papai")