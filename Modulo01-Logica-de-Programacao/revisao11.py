'''11. Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.'''

anos = int(input("Quantos anos voce viveu? "))
meses = int(input("Quantos meses voce viveu? "))
dias = int(input("Quantos dias voce viveu? "))
idade = anos*365 + meses*30 + dias
print(f'Voce viveu por {idade} dias.')