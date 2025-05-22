import os
os.system("cls || clear")

contador = 0
soma = 0

while True:
    nota = float(input("Informe a nota: "))
    pergunta = (input(f"\nDeseja adicionar mais alguma nota ? \nDigite 'N' ou 'S': ")).upper()
    
    if pergunta == "n":
        break
    else: 
        contador += 1
        soma += nota

#Evita divisão por zero.
if contador == 0:
   soma = nota
   contador = 1

media = soma / contador

print(f"\nMédia: {media}")