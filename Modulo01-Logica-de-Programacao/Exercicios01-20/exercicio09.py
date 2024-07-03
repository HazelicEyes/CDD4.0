combustivel = input("Escolha o tipo de combustivel (E = Etanol ou G = Gasolina):")
L = float(input("Quantos litros de combustivel a serem abastecidos? "))
E = 4.90
G = 5.80


if combustivel == "E" or combustivel == "e":
    totalE = E*L
    print(f"O total a ser pago de etanol vai ser {totalE} reais")
elif combustivel == "G" or combustivel == "g":
    totalG = E*G
    print(f"O total a ser pago de gasolina vai ser {totalG} reais")
else:
    print("COMBUSTIVEL INVALIDO")
