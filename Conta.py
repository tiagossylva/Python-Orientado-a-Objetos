class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if (saldo<0):
            print("o saldo não pode ser negativo")
        else:
            selef._saldo = saldo

    def saque( self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("saque realizado com sucesso")
        else:
            print("saldo insuficiente")
            
    def deposita(self, valor):
        self.saldo+=valor

    def extrato(self):
        print("cliente: ", self.titular, "saldo atual: ", self.saldo)
