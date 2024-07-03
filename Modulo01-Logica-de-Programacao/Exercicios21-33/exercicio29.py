notas = [0,0,0,0,0]
soma = 0
contador = 0
for x in range(len(notas)):
    notas[x] = float(input("Digite as notas dos alunos: "))

for y in range(len(notas)):
    soma += notas[y]
media = soma / 5

for z in range(len(notas)):
    if notas[z] >= media:
        contador += 1
print(f'A media da sala é {media}')
print(f'A quantidade de alunos que tiveram a nota maior ou igual que a media é {contador}')