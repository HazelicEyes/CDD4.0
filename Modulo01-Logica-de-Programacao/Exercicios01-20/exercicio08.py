time1 = input("Nome primeiro time: ")
gol_time1 = int(input("Numero de gols do primeiro time: "))
time2 = input("Nome segundo time: ")
gol_time2 = int(input("Numero de gols do segundo time: "))

if gol_time1 > gol_time2:
    print("O time vencedor é o:", time1)
elif gol_time2 > gol_time1:
    print("O time vencedor é o:", time2)
else:
    print("EMPATE")