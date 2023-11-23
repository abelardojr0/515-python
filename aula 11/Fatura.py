class Fatura:
  def __init__(self, nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade
  
  def gerar_fatura(self):
    valor_total = self.preco * self.quantidade
    return valor_total

fatura1 = Fatura(nome="Mouse", preco=25, quantidade=50)

print(f"O valor total da fatura é: {fatura1.gerar_fatura()}")

    