class Atleta:
    def __init__(self):
        self.aposentado = False
        self.aquecido = False
        self.peso = 0

    def aposentar(self):
        if self.aposentado is False:
            self.aposentado = True
            print(f'O atleta foi APOSENTADO. Bom descanso.')
        else:
            print(f'O atleta ja esta APOSENTADO.')

    def aquecer(self):
        if self.aquecido is False:
            self.aquecido = True
            print(f' O atleta esta AQUECENDO.')

class Corredor(Atleta):
    def __init__(self):
        super().__init__()
    def correr(self):
        if self.aposentado is False:
            if self.aquecido is True:
                print(f' O atleta esta CORRENDO')
            else:
                print(f' O atleta não pode correr porque não aqueceu.')
        else:
            print(f' O atleta não pode correr porque esta aposentado.')

class Nadador(Atleta):
    def __init__(self):
        super().__init__()
    def nadar(self):
        if self.aposentado is False:
            if self.aquecido is True:
                print(f' O atleta esta NADANDO')
            else:
                print(f' O atleta não pode NADAR porque não aqueceu.')
        else:
            print(f' O atleta não pode NADAR porque esta aposentado.')

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()
    def pedalar(self):
        if self.aposentado is False:
            if self.aquecido is True:
                print(f' O atleta esta PEDALANDO')
            else:
                print(f' O atleta não pode PEDALAR porque não aqueceu.')
        else:
            print(f' O atleta não pode PEDALAR porque esta aposentado.')

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self):
        super().__init__()

#atividade casa = para o atleta fazer qualoquer acao, ele tem que aquecer e nao estar aposentado