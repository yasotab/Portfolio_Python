import datetime

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # 'depósito' ou 'saque'
        self.valor = valor
        self.data = datetime.datetime.now()

    def __str__(self):
        return f"{self.data}: {self.tipo} de R${self.valor:.2f}"

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor do depósito deve ser positivo.")
            return
        self.saldo += valor
        transacao = Transacao('depósito', valor)
        self.historico.append(transacao)
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor do saque deve ser positivo.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        self.saldo -= valor
        transacao = Transacao('saque', valor)
        self.historico.append(transacao)
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def mostrar_historico(self):
        print(f"Histórico de transações de {self.titular}:")
        for transacao in self.historico:
            print(transacao)

    def mostrar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

# Exemplo de uso
if __name__ == "__main__":
    conta = ContaBancaria("João Silva")
    conta.depositar(500)
    conta.sacar(200)
    conta.mostrar_historico()
    conta.mostrar_saldo()