contador = 0
for x in range(10):
    n = int(input("Insira um numero: "))
    if n <0:
        contador = contador + 1
print(contador,"negativos")