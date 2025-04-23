import os 
os.system ("cls || clear")

QUANTIDADE_NUMEROS = 5

def solicitar_dados():
    lista_numeros = []
    for i in range (QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numero)
    return lista_numeros

def verificar_positivos_negativos(lista):
    soma_positiva = 0
    negativos = 0
    for numero in lista: 
        if numero < 0:
            negativos +=1
        else:
            soma_positiva += numero
    return negativos, soma_positiva

lista = solicitar_dados()
negativos, soma_positiva = verificar_positivos_negativos(lista)

print(f"\nQuantidade de números negativos: {negativos}")
print(f"Soma de números positivos {soma_positiva}")