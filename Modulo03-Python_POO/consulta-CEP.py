import requests #isso aqui precisa instalar

print("Verificando endereço")
cep = input("Digite seu CEP: ")
if len(cep) !=8:
    print('CEP INVALIDO. Terminando o programa.')
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(consulta.json())