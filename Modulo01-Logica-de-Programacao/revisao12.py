'''12. Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores.'''

eleitores = int(input("Digite o numero de eleitores: "))
validos = int(input("Digite o numero de votos validos: "))
brancos = int(input("Digite o numero de votos brancos: "))
nulos = int(input("Digite o numero de votos nulos: "))

percentualValidos = (validos/eleitores)*100
percentualBrancos = (brancos/eleitores)*100
percentualNulos = (nulos/eleitores)*100

print(f'----RESULTADO DOS VOTOS----'
      f'\n{percentualValidos}% dos votos sao validos'
      f'\n{percentualBrancos}% dos votos sao brancos'
      f'\n{percentualNulos}% dos votos sao nulos')

