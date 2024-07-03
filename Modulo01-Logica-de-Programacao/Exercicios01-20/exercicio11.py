'''entrada1 = 3:45
entrada2 = 14:20
saida = 6:05'''

hora1 = int(input("Digite a primeira hora: "))
minutos1 = int(input("Digite os primeiros minutos: "))
hora2 = int(input("Digite a segunda hora: "))
minutos2 = int(input("Digite os segundos minutos: "))

horasaida = hora1 + hora2
minutosaida = minutos1 + minutos2

if minutosaida >= 60:
    horasaida = horasaida ++ 1
    minutosaida = minutosaida - 60
if horasaida >= 24:
    horasaida = horasaida - 24
if horasaida > 12:
    horasaida = horasaida - 12
if horasaida > 12:
    horasaida = horasaida - 12

print(f'{horasaida}:{minutosaida}')