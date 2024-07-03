'''15. Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

if n1 > n2:
    print(f'{n2} e {n1}')
else:
    print(f'{n1} e {n2}')
