import os
os.system("cls || clear")

def diferenca(numero):
    if numero <0 :
        print("Número negativo. ")  
    elif numero == 0: 
        print(f"NÚMERO NEUTRO IDENTIFICADO ({numero})") 
    else:
        print("Número inteiro. ")

print(f"\t= Números Negativos ou Positivos =")
numero = int(input(f"\nDigite um número: "))
diferenca(numero)

