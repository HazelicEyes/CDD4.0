nomes = ['', '', '', '', '']
senhas = ['', '', '', '', '']

menu = 0
while menu != 3:
    menu = int(input("MENU: (1) CADASTRO - (2) LOGIN - (3) SAIR \nDigite um numero: "))
    if menu ==1:
        for x in range(5):
            nomes[x] = input(f'Digite o nome do {x + 1}º usuario: ')
            senhas[x] = input(f'Digite a senha do {x + 1}º usuario: ')
        print(f'Cadastro de {nomes[x]} efetuado com sucesso')
    elif menu ==2:
        usuario = input("Digite seu nome: ")
        login = input("Digite a sua senha: ")
        for y in range(5):
            if usuario == nomes [y] and login == senhas[y]:
                print(f"Login efetuado com sucesso. Seja bem vindo {nomes[y]}.")
                exit()
        else:
            print("Senha incorreta, usuario não encontrado")
    elif menu ==3:
        print("Saindo do sistema")
    else:
        print("Numero invalido")

