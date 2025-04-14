import os 
import time
os.system("cls || clear")

listagem = []
QUANTIDADE_NUMEROS = 4

for i in range (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite {i+1}º número: "))
    listagem.append(numero) 

# Verificando maior e menor número em uma lista.
# As funções max() e min() percorrem o vetor e mostram o maior e
# o menor número respectivamente
maior =  max(listagem)
menor =  min(listagem)    

print(f"\n\t= Mostrando Números =")
# Usando ForEach numerando os elementos da lista.
# Iniciando contagem com a variável i, comeando pelo número 1.
for i, numero in enumerate(listagem, start=1):
    print(f"{i}º número: {numero}")
    time.sleep(5)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

