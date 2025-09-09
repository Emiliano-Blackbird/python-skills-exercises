class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        self.saldo -= cantidad
        print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")

    def mostrar_saldo(self):
        print(self.__dict__)


cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(200)

cuenta2 = CuentaBancaria("María Gómez", 2000)
cuenta2.mostrar_saldo()
cuenta2.depositar(300)
cuenta2.retirar(1000)
