from classes import *

p1 = Pessoa("Joao",65,23)
p2 = Pessoa("Maria",55,20)

print(f'O nome da pessoa 1 é {p1.nome} e ela pesa {p1.peso}')
p1.nome = "Henrique"

p1.falar("Alguma coisa")
p1.comer("Coxinha")
p1.pararDeFalar()
p1.comer("Coxinha")

p1.falar("Alguma coisa 2")
p1.pararDeComer()
p1.falar("Alguma coisa 2")

p1.dormir()
p1.pararDeFalar()
p1.dormir()
p1.falar("Oi, bom dia prof")
p1.acordar()
p1.falar("ALO")


