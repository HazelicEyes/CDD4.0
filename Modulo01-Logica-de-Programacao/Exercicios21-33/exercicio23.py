n1 = float(input("Digite o primeiro valor : "))
n2 = float(input("Digite o segundo valor : "))
while n2 == 0:
    n2 = float(input("Não pode digitar zero, digite outro valor: "))
    
divisao = n1 / n2
print(f"A divisão de {n1} por {n2} é {divisao}")