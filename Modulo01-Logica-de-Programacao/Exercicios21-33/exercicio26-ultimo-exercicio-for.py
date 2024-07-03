""" metodo com 1 for
num = int(input("Digite um numero: "))

for x in range(1,num+1):
    print(str(x)*x, end= " ")

"""
num = int(input("Digite um numero: "))
for x in range(1,num+1):
    for y in range(1,x+1):
        print(x, end = " ")
    print()