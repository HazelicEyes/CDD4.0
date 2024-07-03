'''17.As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem
compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e
escreva o custo total da compra'''

macas = int(input("Digite o numero de maçãs que vc deseja comprar: "))
preco1 = 1.30
preco2 = 1.00

if macas < 12:
    total = macas * preco1
    print(f'O preço de {macas} maçãs sai por {total} reais')
else:
    total = macas * preco2
    print(f'O preço de {macas} maçãs sai por {total} reais')
