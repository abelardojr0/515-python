class Televisao:
  def __init__(self, marca:str, polegadas:int, smart:bool, preco: float, apps: list):
    self.marca = marca
    self.polegadas = polegadas
    self.smart = smart
    self.preco = preco
    self.apps = apps

tv1 = Televisao(marca="LG", polegadas=50, smart=True, preco=2.149, apps=["Netflix, Youtube, Google"])
    