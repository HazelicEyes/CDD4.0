nomes = ['','','','','']
senhas = ['','','','','']

for x in range(5):
    nomes[x] = input(f'Digite o nome do {x+1}º usuario: ')
    senhas[x] = input(f'Digite a senha do {x+1}º usuario: ')

for y in range(5):
    print(f'Nome: {nomes[y]}, Senha: {senhas[y]}, Posição: {y}')
