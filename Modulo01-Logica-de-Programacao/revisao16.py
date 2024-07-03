'''16. Escreva um algoritmo para ler a hora de
início e a hora de ﬁm de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia'''

inicio = int(input("Digite o horario de inicio: "))
final = int(input("Digite o horario de fim: "))

if inicio < final:
    duracao = final - inicio
else:
    duracao = 24 - inicio + final

print(f"A partida durou {duracao} horas")