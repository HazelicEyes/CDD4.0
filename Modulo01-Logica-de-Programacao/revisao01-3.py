# 1.Faça um algoritmo que receba 2
# notas e calcule a média aritmética

nota1 = float(input("Digite a primeira nota: "))
while nota1 <0 or nota1 >10:
    nota1 = float(input("Nota1 invalida, digite apenas de 0 a 10: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 <0 or nota2 > 10:
    nota2 = float(input("Nota2 invalida, digite apenas de 0 a 10: "))

media = (nota1 + nota2) / 2
print(f'A media é {media}.')

