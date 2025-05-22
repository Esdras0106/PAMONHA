import os
os.system("cls || clear")

QUANTIDADE_DE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input("Digite a nota: "))
        
        if nota <0 or nota >10:
            nota = ("Ação negada, a nota deve estar entre 0 e 10.")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_DE_NOTAS

if media <6 and media >4:
    print("RECUPERAÇÃO!")
elif media <=4:
    print("REPROVADO.")
else:
    print("APROVADO.")

print(f"Média aritimetica: {media}")

