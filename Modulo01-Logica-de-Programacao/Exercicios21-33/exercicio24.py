pin = "1234"
senha = input("Digite a senha: ")
contador = 1

if senha != pin:
    while senha != pin:
        if senha != pin and contador == 3:
            print("Acesso bloqueado, errou 3x")
            break
        contador +=1
        senha = input ("Senha errada, digite novamente: ")
    else:
        print("Acesso liberado")
else:
    print("Acesso liberado")


'''pin = "1234"
senha = input("Digite a senha: ")
contador = 1

if senha == pin:
    print("Senha correta, acesso liberado")
while senha != pin:
    input("Senha incorreta, digite novamente: ")
    contador += 1
    if contador >= 3 and senha == pin:
        print("Senha correta, acesso liberado")
        break
    elif contador == 3 and senha != pin:
        print("Errou a senha 3 vezes, acesso bloqueado")
        break
'''