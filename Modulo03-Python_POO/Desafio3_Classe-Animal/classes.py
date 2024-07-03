class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'O {self.nome} foi comer.')

    def correr(self):
        print(f'O {self.nome} esta correndo.')  # abaixo começa a parte de herança


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f'O {self.nome} esta miando.')


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'O {self.nome} esta latindo.')

    def morder(self):
        print(f' O {self.nome} mordeu a pessoa.')


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f'O {self.nome} esta pulando.')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f'O {self.nome} esta mugindo.')
