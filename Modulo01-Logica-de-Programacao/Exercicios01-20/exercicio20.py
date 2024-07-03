soma = 0
divisao = 10
for x in range(10):
    n = float(input("Insira um valor: "))
    if n >= 0 and n <= 10:
        soma = soma + n
    else:
        divisao = divisao -1
if divisao == 0:
    print("Não ha valor para dividir, todos os numeros estao errados")
else:
    media = soma / divisao
    print(f"A media aritmetica é {media}")