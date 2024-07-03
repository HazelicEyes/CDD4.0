a = [0,0,0,0,0,0,0,0,0,0]
m = [0,0,0,0,0,0,0,0,0,0]

for x in range(10):
    a[x] = int(input(f"Digite o {x+1}º numero: "))
multiplicador = int(input("Digite o numero pelo qual voce quer multiplicar as notas: "))

for y in range(10):
    m[y] = a[y] * multiplicador
print(a)
print(multiplicador)
print(m)