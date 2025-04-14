import os 
os.system("cls || clear")

def calc_media(media):
    media = sum(lista_notas) / QUANTIDADE_NOTAS
    return media

def condicao (media):   
    if media >= 5:
        resultado = (f"Em Recuperação.")
    elif media <5:
        resultado = (f"Reprovado.")
    else:
        resultado = (f"Aprovado.")   
    return resultado

lista_notas = []
QUANTIDADE_NOTAS = 3

for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota) 

media = calc_media(lista_notas)
resultado = condicao(media)

print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")

