class Main:
    pass
from Cliente import Cliente
from Conta import Conta

c1 = Cliente("joão", "11444-2222")
conta = Conta(c1.get_nome(), 1222,0)

conta.deposita(100)
conta.saque(50)
conta.extrato()

print(conta.titular, "numero: ", conta.numero, "seu saldo: ", conta.saldo)
