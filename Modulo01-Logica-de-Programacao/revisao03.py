'''3. Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu'''


ano = 2024
idade = int(input("Digite a idade: "))
aniversario = input("Voce ja fez aniversario esse ano? (s/n): ")
if aniversario == 'n' or aniversario == 'N':
    ano = ano -1
nascimento = ano - idade
print(f'A pessoa nasceu em {nascimento}')