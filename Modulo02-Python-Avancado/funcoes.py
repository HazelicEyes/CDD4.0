def imprime_nome(nome):
    print(f'Nome: {nome}')
def piramide(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(x, end=" ")
        print()
def piramide2(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()
def contar_vogais(texto):
    contador = 0
    vogais = 'aeiouAEIOU'
    for x in texto:
        if x in "aeiouAEIOU":
            contador += 1
    print(contador)
def estoque(produto, quantidade, valor):
    total = valor*quantidade
    return total
def numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0 :
        return 'Negativo'
    else:
        return 'Zero'
def somar(n1,n2):
    soma = n1+n2
    return soma
def somar2(*num):
    soma = 0
    for x in range(len(num)):
        soma = soma + num[x]
    print(soma)
def texto(texto):
    #imprimir letra pro letra
    for a in range(len(texto)):
        print(texto[a], end ='')

    # contar quantas letras
    contador = 0
    for x in texto:
        if x not in " .,!":
            contador = contador + 1
    print(f'\nO texto <{texto}> tem {contador} letras')

    # imprimir ao contrario
    for y in range (len(texto)-1,-1,-1):
        print(texto[y], end ='')
def lista(lista):
    novaLista = []
    for x in range(len(lista)):
        if lista[x] not in novaLista:
            novaLista.append(lista[x])
    print(novaLista)
    '''    
    novaLista = set(lista)
    print(novaLista)
    '''
def primo(numero):
    if numero == 1:
        return numero, "Não é primo"
    elif numero == 2:
        return numero, "É primo"
    else:
        for x in range(2,numero):
            if (numero % x == 0):
                return numero, "Não é primo"
        return numero, "É primo"
