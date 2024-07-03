'''7. Faça um código que receba o valor da
base e da altura de um triângulo e
calcule sua área. usando a fórmula A =
(base x Altura ) /2'''


pergunta = 0
while pergunta != 3:
    pergunta = int(input("MENU: (1) Calculo para triangulo -- (2) Calculo para quadrado -- (3) Sair do sistema "
                         "\nDigite um numero: "))
    if pergunta == 1:
        base = float(input("Digite a base do triangulo: "))
        altura = float(input("Digite a altura do triangulo: "))
        multi = base * altura
        area = multi / 2
        print(f'A Area do triangulo de base {base} por altura {altura} é igual a {area}.')
    elif pergunta == 2:
        quadrado = float(input("Digite o lado do quadrado: "))
        areaQuadrado = quadrado**2
        print(f'A area do quadrado é {areaQuadrado}')
    elif pergunta == 3:
        print("Saindo do sistema")
    else:
        print("Numero invalido, digite apenas 1, 2 ou 3\n ")