class Pessoa():
# Classes tem Metodos e Atributos, (Metodos sao Funcoes e Atributos são Variaveis)
    def __init__(self, nome, peso, idade): # metodo construtor e parametros
        self.nome = nome
        self.peso = peso #esses 3 são atributos #atributos usam sempre self, atributos atribuem valores
        self.idade = idade
        self.acao = "nenhum"
    def falar(self, falar):
        if self.acao == "nenhum":
            self.acao = "falando"
            print(f'{self.nome} esta falando <{falar}>')
        else:
            print(f'{self.nome} não pode falar <{falar}> porque esta <{self.acao}>')
    def pararDeFalar(self):
        if self.acao == "falando":
            self.acao = "nenhum"
            print(f'{self.nome} parou de falar')

    def comer(self, comida):
        if self.acao == "nenhum":
            self.acao = "comendo"
            print(f'{self.nome} esta comendo <{comida}>')
        else:
            print(f'{self.nome} não pode comer <{comida}> porque esta <{self.acao}>')
    def pararDeComer(self):
        if self.acao == "comendo":
            self.acao = "nenhum"
            print(f'{self.nome} parou de comer')

    def dormir(self):
        if self.acao == "nenhum":
            self.acao = "dormindo"
            print(f'{self.nome} foi <dormir>.')
        else:
            print(f'{self.nome} não pode <dormir> porque esta <{self.acao}>')
    def acordar(self):
        if self.acao == "dormindo":
            self.acao = "nenhum"
            print(f'{self.nome} <acordou>')
