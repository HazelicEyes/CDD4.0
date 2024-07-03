'''4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.'''

anterior = 0
for x in range(3):
    numero = int(input(f'Digite o {x+1}º numero: '))
    if numero > anterior:
        anterior = numero
print(f'O numero {anterior} é maior')