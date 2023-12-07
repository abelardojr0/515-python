class Conta:
    def __init__(self, numero, nome, banco, saldo) -> None:
        self.numero = numero
        self.nome = nome
        self.banco = banco
        self.saldo = saldo
    
    def deposito(self, valor_do_deposito):
        self.saldo = self.saldo + valor_do_deposito
        return self.saldo
    
conta1 = Conta(numero=123456, nome="Joao", banco="Nubank", saldo=1000)

conta1.deposito(500)
