import os 
os.system ("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5
negativos = 0
soma_negativa = 0
soma_positiva = 0

for i in range (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

for numero in lista_numeros: 
    if numero < 0:
        negativos +=1
    else:
        soma_positiva += numero

print(f"\nQuantidade de números negativos: {negativos}")
print(f"Soma de números positivos {soma_positiva}")