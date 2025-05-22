import os
os.system("cls || clear")

def calc_media(nota1, nota2):
    soma = nota1 + nota2 
    resultado = soma / 2
    return resultado

def calcular_resultado(media):
    if media >=7 :
        print("Aprovado.")
    else:
        print("Reprovado.")

print(f"\t= NOTAS =")
nota1 = float(input(f"\nDigite a 1ª nota: "))
nota2 = float(input(f"Digite a 2ª nota: "))

media = calc_media(nota1, nota2)
calcular_resultado(media)

