import os
os.system ("cls || clear")

listagem = []
QUANTIDADE_NUMEROS = 5
soma_valores = 0

for i in range (QUANTIDADE_NUMEROS):
    valor = int(input("Informe um valor: "))
    listagem.append(valor)
    if valor < 0:
        valor = 0 

print("= LISTANDO NÚMEROS =")

for valor in listagem:
    print(f"Valores: {valor}")