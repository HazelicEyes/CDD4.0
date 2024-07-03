# 1.Faça um algoritmo que receba 2
# notas e calcule a média aritmética

soma = 0
for x in range(2):
    nota1 = float(input(f'Digite a {x+1} nota: '))
    while nota1 < 0 or nota1 >10:
        nota1 = float(input("Nota invalida, digite apenas numeros de 0 a 10: "))
    soma = soma + nota1

media = soma / 2
print(f'A media é {media}.')