import random
class Jogar:
    def __init__(self):
        self.escolhaUsuario = 'None'
        self.escolhaComputador = random.choice(['pedra', 'papel', 'tesoura'])

    def pedra(self):
        self.escolhaUsuario = 'pedra'
        if self.escolhaUsuario == self.escolhaComputador:
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO jogo deu EMPATE.')
        elif self.escolhaUsuario == 'pedra' and self.escolhaComputador == 'tesoura':
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO usuario VENCEU.')
        else:
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO usuario PERDEU.')
    def papel(self):
        self.escolhaUsuario = 'papel'
        if self.escolhaUsuario == self.escolhaComputador:
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO jogo deu EMPATE.')
        elif self.escolhaUsuario == 'papel' and self.escolhaComputador == 'pedra':
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO usuario VENCEU.')
        else:
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO usuario PERDEU.')
    def tesoura(self):
        self.escolhaUsuario = 'tesoura'
        if self.escolhaUsuario == self.escolhaComputador:
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO jogo deu EMPATE.')
        elif self.escolhaUsuario == 'tesoura' and self.escolhaComputador == 'papel':
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO usuario VENCEU.')
        else:
            print(f'O usuario escolheu <{self.escolhaUsuario}>, o computador escolheu <{self.escolhaComputador}>'
                  f'\nO usuario PERDEU.')
