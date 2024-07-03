pergunta = "s"
while pergunta == "s" or pergunta == "S":
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 <0 or nota1 >10:
        nota1 = float(input("Nota incorreta, digite novamente a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 <0 or nota2 >10:
        nota2 = float(input("Nota incorreta, digite novamente a segunda nota: "))

    media = (nota1+nota2) / 2
    print(f"A media é {media}")
    pergunta = input("Deseja continuar? S para sim e N para não: ")
else:
    print("Ok, tenha um bom dia")