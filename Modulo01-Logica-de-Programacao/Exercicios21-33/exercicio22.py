soma = 0
contador = 0
alunos = int(input("Digite o numero de alunos: "))
while contador != alunos:
    notas = float(input("Digite as notas desses alunos: "))
    soma = soma + notas
    contador = contador + 1
    print("A soma atual é", soma)
media = soma / alunos
print(f"A media dos {alunos} alunos da sala é {media}")