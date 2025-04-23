import os
import time
os.system("cls || clear")

listagem = []
QUANTIDADE_NUMEROS = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        
        if numero %2 == 0:
            pares += 1

        else:
            impares += 1

    print(f"\n= ITENS DA LISTA =")
    for i, numero in enumerate(listagem, start=1):
        print(f"{i}: {numero}")
    
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")


