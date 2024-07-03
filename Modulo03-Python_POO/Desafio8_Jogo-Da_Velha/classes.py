import random
class JogoDaVelha:
    tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}
    turno = None
    escolha = None

    def __init__(self):
        while True:
            self.escolha = int(input("Vai querer jogar contra outro jogador ou contra o computador?"
                        "\nDigite 1 para outro jogador / 2 para computador: "))
            if self.escolha == 1:
                jogador_inicial = input("Certo. Nesse jogo voce começa primeiro,"
                                        " vai querer jogar com X ou O? ")
                jogador_inicial = jogador_inicial.upper()
                self.turno = jogador_inicial
                self.escolha = 1

                while jogador_inicial not in "XxOo":
                  jogador_inicial = input("Letra invalida, digite apenas X ou O: ")
                  jogador_inicial = jogador_inicial.upper()
                  self.turno = jogador_inicial
                break
            elif self.escolha == 2:
                print('Começando o jogo contra o computador.'
                      '\nPor padrão, X é o usuario, O é o computador e ele começa primeiro.')
                self.turno = 'O'
                self.escolha = 2
                break
            else:
                print('\nEscolha errada, digite somente 1 ou 2')


    def exibir_tabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    def verificar_tabuleiro(self):
        # Verificações das 3 verticais
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']


        # Verificações das 3 horizontais
        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']

        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']

        # Verificando empate
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.tabuleiro.values()].count(' ')

    def jogar(self):
        '''print("Bom dia usuario! Devido a limitações no codigo voce vai jogar com X e o computador com O."
              "\ne não, eu não vou mudar isso. Bom jogo!")'''
        #depois de 3 xicaras de cafe e 3 horas quebrando a cabeça, acabou que eu alterei :)
        while True:
            self.exibir_tabuleiro()
            if self.escolha == 1:
                print(f"Turno do {self.turno}, qual sua jogada? "
                  f"(As posições são as mesmas do teclado numerico.)")
            # Enquanto o jogador não fizer uma jogada válida
            while True:
                jogada = None
                if self.turno == 'O' and self.escolha == 2:
                    jogada = random.choice(["1","2","3","4","5","6","7","8","9"])
                elif self.turno == 'X' and self.escolha == 2:
                    jogada = input("Seu turno, jogador X. (As posições são as mesmas do teclado numerico.) "
                                   "\nQual sua jogada? ")
                else:
                    jogada = input("Jogada: ")

                if self.verificar_jogada(jogada):  # Se a jogada for válida...
                    if self.turno == 'O' and self.escolha == 2:
                        print(f'O computador jogou na posição {jogada}.')
                    break  # Encerra o loop
                else:
                    if self.escolha == 1 or self.escolha == 2 and self.turno == "X":
                        print(f"\njogada do {self.turno} inválida, jogue novamente.")

            self.tabuleiro[jogada] = self.turno
            estado = self.verificar_tabuleiro()

            if estado == "X":
                print("X é o vencedor!!!")
                break
            elif estado == "O":
                print("O é o vencedor!!!")
                break
            if estado == "empate":
                print("EMPATE!!!")
                break
            # Troca o jogador do próximo turno
            self.turno = "X" if self.turno == "O" else "O"

        self.exibir_tabuleiro()