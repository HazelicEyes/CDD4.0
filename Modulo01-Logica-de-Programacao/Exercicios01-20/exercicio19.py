dentro = 0
fora = 0
for x in range(10):
    n = int(input("Insira um numero: "))
    if n >= 10 and n <=20:
        dentro += 1
    else:
        fora += 1
print(dentro,"numeros estão no intervalo de 10 e 20")
print(fora,"numeros estão fora do intervalo")