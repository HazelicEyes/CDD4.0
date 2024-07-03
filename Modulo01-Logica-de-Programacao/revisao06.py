'''6. Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10'''

numero = int(input("Digite um valor: "))
if numero > 10:
    print(f'O numero {numero} é maior que 10.')
else:
    print(f'O numero {numero} não é maior que 10.')
