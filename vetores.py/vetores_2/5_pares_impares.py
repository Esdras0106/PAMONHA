import os
os.system("cls || clear")

def limpar():
    import os
    os.system("cls || clear")

listagem = []
QUANTIDADE_NUMEROS = 6
pares = 0
impares = 0

print("= LISTA DE NÚMEROS =")
for i in range (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    listagem.append(numero)

    if numero %2 == 0:
        pares += 1

    else:
        impares += 1

print(f"\n= ITENS DA LISTA =")
for i, numero in enumerate(listagem, start=1):
    print(f"{i}: {numero}")

print(f"Pares: {pares}")
print(f"Impares: {impares}")


