'''4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.'''

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > n2:
    if n1 > n3:
        print(f'{n1} é maior')
    else:
        print(f'{n3} é maior')
elif n2 > n3:
        print(f'{n2} é maior')
else:
     print(f'{n3} é maior')