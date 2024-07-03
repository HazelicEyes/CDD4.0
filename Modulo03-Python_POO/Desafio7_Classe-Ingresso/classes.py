class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'Um ingresso NORMAL custa R${self.valor}.')

class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeValor(self): #polimorfismo é mudar a parte do codigo que é herdado, nome dos metodos sao iguais
        valorVip = self.valor*1.5
        print(f'Um ingresso VIP custa R${valorVip}.')
