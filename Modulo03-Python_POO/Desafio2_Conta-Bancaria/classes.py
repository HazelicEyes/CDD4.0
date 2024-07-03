class Conta():
    def __init__(self, numeroConta, nomeCliente): # metodo construtor e parametros
        self.numero = numeroConta
        self.nome = nomeCliente
        self.saldo = 0.0
        self.conta = 'nomeConta' # atributos tem self
        self.tipo = 'tipoConta'
        self.statusConta = False
    def ativarConta(self):
        if self.statusConta == False:
            self.statusConta = True
            print(f'A conta foi ATIVADA com sucesso.')
        else:
            print(f'A conta ja esta ativada')
    def desativarConta(self):
        if self.statusConta == True:
            if self.saldo == 0:
                self.statusConta = False
                print(f'Conta DESATIVADA com sucesso.')
            else:
                print(f'Não foi possivel desativar a conta porque ainda tem saldo nela.')
        else:
            print(f'A conta ja foi desativada..')
    def criarConta(self):
        self.conta = input("Digite o nome da conta que quer criar: ")
        self.tipo = input("Digite o tipo da conta que quer criar\n (C para Corrente -- P para poupança): ")
    def depositar(self, depositar):
        if self.statusConta == True:
            self.saldo = self.saldo + depositar
            print(f'Depositado com sucesso o valor de R${depositar}.')
        else:
            print(f'Não foi possivel depositar dinheiro porque a conta esta <INATIVA>.')
    def sacar(self, sacar):
        if self.statusConta == True and self.saldo != 0:
            if sacar > self.saldo:
                print(f'Não foi possivel sacar porque o valor de R${sacar} ultrapassa o saldo na conta de R${self.saldo}.')
            else:
                self.saldo = self.saldo - sacar
                print(f'Sacado com sucesso o valor de R${sacar}.\n Saldo atual é R${self.saldo}.')
        else:
            print(f'Não foi possivel sacar porque não ha saldo.')
    def verificarSaldo(self):
        print(f'O saldo na conta é de R${self.saldo}.')